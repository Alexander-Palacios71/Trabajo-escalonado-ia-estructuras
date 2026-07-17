import re
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.signal import detrend, butter, filtfilt

# Configuración global para el módulo 4
PARAMETROS_NORMATIVOS = {
    "zona": 3,
    "uso": "C",
    "suelo": "S3",
    "R": 1.0,
}

class RegistroSismico:

    def __init__(self):
        # Información general
        self.evento = ""
        self.estacion = ""
        self.codigo = ""
        self.magnitud = None
        self.latitud = None
        self.longitud = None
        self.frecuencia = None
        self.dt = None
        self.numero_muestras = None
        self.tiempo_en_columna = False
        self.tiempo_derivado = False

        # Componentes
        self.componente_ew = "EW"
        self.componente_ns = "NS"
        self.componente_ud = "UD"

        # DataFrames
        self.datos = pd.DataFrame()
        self.espectros = pd.DataFrame()
        self.parametros_normativos = {}

    # =========================================================================
    # MÓDULO 0: LECTURA DE DATOS
    # =========================================================================
    def _buscar_frecuencia_desde_encabezado(self, lineas):
        for linea in lineas:
            texto = linea.strip().lower()
            if ":" not in linea:
                continue
            if "sampling frequency" in texto or "frequency (hz)" in texto or "frequency" in texto:
                if "record time" in texto or "origin time" in texto:
                    continue
                num = re.findall(r"\d+(?:\.\d+)?", linea)
                if num:
                    return float(num[0])
        return None

    def _detectar_columna_tiempo(self, lineas):
        for i, linea in enumerate(lineas):
            if "ACCELERATION DATA" not in linea.upper():
                continue

            for offset in range(1, 4):
                if i + offset >= len(lineas):
                    break
                encabezado = lineas[i + offset].strip()
                if not encabezado:
                    continue
                texto = encabezado.lower()
                if re.search(r"\b(t|time)\b", texto):
                    return True

            return False

        return False

    def _leer_encabezado_datos(self, lineas, index_inicio):
        for linea in lineas[index_inicio:]:
            if not linea.strip():
                continue
            tokens = [re.sub(r"[^a-z]", "", token).upper() for token in linea.split() if token.strip()]
            if any(token in {"T", "TIME", "EW", "NS", "UD"} for token in tokens):
                return tokens
        return []

    def cargar_txt(self, ruta_archivo):
        if not os.path.exists(ruta_archivo):
            print(f"❌ Error: No se encontró el archivo '{ruta_archivo}'.")
            return

        print("  Leyendo archivo...")
        with open(ruta_archivo, "r", encoding="utf8", errors="ignore") as f:
            lineas = f.readlines()
        
        print(f"  Procesando {len(lineas)} líneas...")
        
        # Extraer metadatos del encabezado
        for linea in lineas:
            texto = linea.strip().lower()
            if "station" in texto and ":" in linea:
                self.estacion = linea.split(":", 1)[1].strip()
            elif "latitude" in texto and ":" in linea:
                num = re.findall(r"[-+]?\d+\.\d+|\d+", linea)
                if num: self.latitud = float(num[0])
            elif "longitude" in texto and ":" in linea:
                num = re.findall(r"[-+]?\d+\.\d+|\d+", linea)
                if num: self.longitud = float(num[0])
            elif "magnitude" in texto and ":" in linea:
                num = re.findall(r"[-+]?\d+\.\d+|\d+", linea)
                if num: self.magnitud = float(num[0])
            elif ("sampling frequency" in texto or "frequency (hz)" in texto or "frequency" in texto) and ":" in linea:
                if "record time" in texto or "origin time" in texto:
                    continue
                num = re.findall(r"\d+(?:\.\d+)?", linea)
                if num:
                    self.frecuencia = float(num[0])
                    self.dt = 1.0 / self.frecuencia
            elif "number of samples" in texto and ":" in linea:
                num = re.findall(r"\d+", linea)
                if num: self.numero_muestras = int(num[0])

        if self.frecuencia is None:
            self.frecuencia = self._buscar_frecuencia_desde_encabezado(lineas)
            if self.frecuencia is not None:
                self.dt = 1.0 / self.frecuencia

        self.tiempo_en_columna = self._detectar_columna_tiempo(lineas)

        # Buscar la sección de datos
        datos = []
        tiempos = []
        data_section_found = False
        
        for i, linea in enumerate(lineas):
            # Buscar "ACCELERATION DATA"
            if "ACCELERATION DATA" in linea.upper():
                data_section_found = True
                # Saltear esta línea y la siguiente (headers)
                data_start_idx = i + 2
                break
        
        if data_section_found and data_start_idx < len(lineas):
            print(f"  Datos encontrados a partir de línea {data_start_idx}")
            encabezado_datos = self._leer_encabezado_datos(lineas, data_start_idx)
            posicion_tiempo = 0
            posicion_ew = 1
            posicion_ns = 2
            posicion_ud = 3

            if encabezado_datos:
                for idx, token in enumerate(encabezado_datos):
                    if token in {"T", "TIME"}:
                        posicion_tiempo = idx
                    elif token == "EW":
                        posicion_ew = idx
                    elif token == "NS":
                        posicion_ns = idx
                    elif token == "UD":
                        posicion_ud = idx

            for linea in lineas[data_start_idx:]:
                cols = linea.split()
                if not cols:
                    continue

                try:
                    valores_num = [float(c) for c in cols]
                except ValueError:
                    if datos:
                        break
                    continue

                if len(valores_num) >= 4:
                    if self.tiempo_en_columna:
                        tiempo_val = valores_num[posicion_tiempo]
                        valores = [
                            valores_num[posicion_ew],
                            valores_num[posicion_ns],
                            valores_num[posicion_ud],
                        ]
                    else:
                        tiempo_val = valores_num[0]
                        valores = valores_num[1:4]
                        self.tiempo_en_columna = True
                        self.tiempo_derivado = False

                    tiempos.append(tiempo_val)
                    datos.append(valores)
                elif len(valores_num) >= 3:
                    valores = valores_num[:3]
                    datos.append(valores)
                    if self.dt is not None:
                        tiempos.append(len(datos) * self.dt)
                        self.tiempo_derivado = True
                    else:
                        tiempos.append(0.0)
                else:
                    continue
        
        if datos:
            datos = np.array(datos)
            if self.dt is None:
                self.dt = 0.005
            if tiempos and len(tiempos) == len(datos):
                tiempo = np.array(tiempos, dtype=float)
            else:
                tiempo = np.arange(len(datos)) * self.dt

            self.datos = pd.DataFrame({
                "Tiempo": tiempo, 
                self.componente_ew: datos[:, 0], 
                self.componente_ns: datos[:, 1], 
                self.componente_ud: datos[:, 2]
            })
            print(f"  Datos cargados: {len(self.datos)} registros")
            if self.tiempo_en_columna:
                print("  Se detectó una columna de tiempo en el archivo.")
            elif self.tiempo_derivado:
                print("  No había columna de tiempo; se construyó la columna T a partir de la frecuencia de muestreo.")
            if self.frecuencia is not None:
                print(f"  Frecuencia de muestreo detectada: {self.frecuencia:.2f} Hz")
        else:
            print("  No se encontraron datos numéricos en el archivo")


    def _guardar_figura(self, fig, nombre_archivo):
        output_dir = os.path.abspath(os.path.dirname(__file__))
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, nombre_archivo)
        fig.savefig(output_path, dpi=100, bbox_inches='tight')
        print(f"  Guardada: {output_path}")
        plt.close(fig)

    # =========================================================================
    # MÓDULO 1: Análisis Exploratorio de Datos (EDA)
    # =========================================================================
    def ejecutar_eda_completo(self):
        if self.datos.empty: return
        print("\n" + "="*50)
        print("INFORME EDA - PRINCIPIOS DE VERIDICAL DATA SCIENCE")
        print("="*50)
        
        nulos = self.datos.isnull().sum().sum()
        if nulos > 0: self.datos.interpolate(method='linear', inplace=True)
        
        pga_ew = self.datos[self.componente_ew].abs().max()
        pga_ns = self.datos[self.componente_ns].abs().max()
        pga_ud = self.datos[self.componente_ud].abs().max()
        
        print(f"PGA EW: {pga_ew:.4f} cm/s² | PGA NS: {pga_ns:.4f} cm/s² | PGA UD: {pga_ud:.4f} cm/s²")
        corr_matrix = self.datos[[self.componente_ew, self.componente_ns, self.componente_ud]].corr()
        self._graficar_eda_visual(corr_matrix)

    def _graficar_eda_visual(self, corr_matrix):
        # Gráfica 1: EDA (No usamos plt.show aquí para que se guarden y abran al final)
        fig = plt.figure(figsize=(14, 10))
        gs = fig.add_gridspec(3, 2, width_ratios=[2, 1])
        
        ax1 = fig.add_subplot(gs[0, 0])
        ax1.plot(self.datos["Tiempo"], self.datos[self.componente_ew], color='#1f77b4', linewidth=0.5)
        ax1.set_title("Componente EW", fontsize=10, weight='bold')
        
        ax2 = fig.add_subplot(gs[1, 0], sharex=ax1)
        ax2.plot(self.datos["Tiempo"], self.datos[self.componente_ns], color='#d62728', linewidth=0.5)
        ax2.set_title("Componente NS", fontsize=10, weight='bold')
        
        ax3 = fig.add_subplot(gs[2, 0], sharex=ax1)
        ax3.plot(self.datos["Tiempo"], self.datos[self.componente_ud], color='#2ca02c', linewidth=0.5)
        ax3.set_title("Componente UD", fontsize=10, weight='bold')
        
        ax_corr = fig.add_subplot(gs[:, 1])
        sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", vmin=-1, vmax=1, fmt=".4f", ax=ax_corr)
        ax_corr.set_title("Matriz de Correlación Símica", fontsize=11, weight='bold')
        
        plt.suptitle("1. Dashboard EDA", fontsize=14, weight='bold')
        plt.tight_layout()
        self._guardar_figura(fig, "grafica_1.png")

    # =========================================================================
    # MÓDULO 2: Procesamiento (Corrección de Línea Base y Filtro)
    # =========================================================================
    def procesar_linea_base_y_filtrado(self, f_low=0.1, f_high=None, orden=4):
        if self.datos.empty: return
        print("\n" + "="*50)
        print("INICIANDO MÓDULO 2: PROCESAMIENTO DE SEÑAL")
        print("="*50)

        nyquist = 0.5 * self.frecuencia
        if f_high is None: f_high = nyquist * 0.95 

        b, a = butter(orden, [f_low/nyquist, f_high/nyquist], btype='bandpass')
        print("Filtro aplicado: Butterworth (Pasa-banda y Fase Cero)")

        for comp in [self.componente_ew, self.componente_ns, self.componente_ud]:
            senal_centrada = detrend(self.datos[comp].fillna(0), type='linear')
            self.datos[f"{comp}_Filt"] = filtfilt(b, a, senal_centrada)

    def graficar_todas_filtradas(self):
        # Gráfica 2: Filtro Estilo SeismoSignal
        if f"{self.componente_ew}_Filt" not in self.datos.columns: return

        fig, axes = plt.subplots(3, 1, figsize=(12, 10), sharex=True)
        colores = ['#1f77b4', '#d62728', '#2ca02c'] 
        comps = [self.componente_ew, self.componente_ns, self.componente_ud]
        nombres = ["Este - Oeste (EW)", "Norte - Sur (NS)", "Vertical (UD)"]
        
        for i, comp in enumerate(comps):
            axes[i].plot(self.datos["Tiempo"], self.datos[comp], color='gray', alpha=0.5, label='Cruda Original', linewidth=1)
            axes[i].plot(self.datos["Tiempo"], self.datos[f"{comp}_Filt"], color=colores[i], label='Filtrada (Línea Base)', linewidth=1)
            axes[i].set_title(f"Componente {nombres[i]}", fontsize=11, weight='bold')
            axes[i].set_ylabel("Acel. (cm/s²)")
            axes[i].legend(loc="upper right")
            axes[i].grid(True, linestyle='--', alpha=0.6)
            
        axes[2].set_xlabel("Tiempo (s)", fontsize=11, weight='bold')
        plt.suptitle("2. Validación de Filtrado de Línea Base", fontsize=14, weight='bold')
        plt.tight_layout()
        self._guardar_figura(fig, "grafica_2.png")

    # =========================================================================
    # MÓDULO 3: ESPECTRO DE RESPUESTA
    # =========================================================================
    def _calcular_newmark_beta(self, acc, dt, periodos, amortiguamiento):
        sa_vals = []
        gamma, beta = 0.5, 1.0 / 6.0 
        
        for T in periodos:
            if T == 0:
                sa_vals.append(np.max(np.abs(acc)))
                continue
                
            w = 2 * np.pi / T
            m = 1.0
            k = m * w**2
            c = 2 * m * w * amortiguamiento
            
            a1 = m / (beta * dt**2) + (gamma * c) / (beta * dt)
            a2 = m / (beta * dt) + (gamma / beta - 1) * c
            a3 = (0.5 / beta - 1) * m + dt * (0.5 * gamma / beta - 1) * c
            k_hat = k + a1
            
            u, v = 0.0, 0.0
            a_acc = -acc[0]
            max_u = 0.0
            
            for i in range(len(acc) - 1):
                p_next = -m * acc[i+1]
                p_hat = p_next + a1*u + a2*v + a3*a_acc
                
                u_next = p_hat / k_hat
                v_next = (gamma/(beta*dt))*(u_next - u) + (1 - gamma/beta)*v + dt*(1 - 0.5*gamma/beta)*a_acc
                a_next = (1/(beta*dt**2))*(u_next - u - dt*v) - (0.5/beta - 1)*a_acc
                
                u, v, a_acc = u_next, v_next, a_next
                if abs(u) > max_u: max_u = abs(u)
                    
            sa_vals.append(w**2 * max_u)
            
        return np.array(sa_vals)

    def generar_espectros(self, amortiguamiento=0.05, t_max=5.0, paso=0.02):
        if f"{self.componente_ew}_Filt" not in self.datos.columns: return

        print("\n" + "="*50)
        print("INICIANDO MÓDULO 3: ESPECTROS DE RESPUESTA")
        print("="*50)

        periodos = np.arange(0.0, t_max + paso, paso)
        self.espectros = pd.DataFrame({"Periodo (T)": periodos})

        comps = [self.componente_ew, self.componente_ns, self.componente_ud]
        for comp in comps:
            acc_filtrada = self.datos[f"{comp}_Filt"].values
            sa_array = self._calcular_newmark_beta(acc_filtrada, self.dt, periodos, amortiguamiento)
            self.espectros[f"Sa_{comp}(cm/s²)"] = sa_array

        self.espectros["Sa_SRSS(cm/s²)"] = np.sqrt(
            self.espectros[f"Sa_{self.componente_ew}(cm/s²)"]**2 + 
            self.espectros[f"Sa_{self.componente_ns}(cm/s²)"]**2
        )
        print("Generación espectral (en cm/s²) exitosa.")

    def graficar_espectros(self):
        # Gráfica 3: Espectro Crudo (Sin Escalar)
        if self.espectros.empty: return

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(self.espectros["Periodo (T)"], self.espectros[f"Sa_{self.componente_ew}(cm/s²)"], color='blue', label='Componente EW', linewidth=1.5)
        ax.plot(self.espectros["Periodo (T)"], self.espectros[f"Sa_{self.componente_ns}(cm/s²)"], color='red', label='Componente NS', linewidth=1.5)
        ax.plot(self.espectros["Periodo (T)"], self.espectros["Sa_SRSS(cm/s²)"], color='black', linestyle='--', label='Combinación SRSS', linewidth=2)

        ax.set_title("3. Espectro de Respuesta del Sismo Filtrado (Sin Escalar)", fontsize=14, weight='bold')
        ax.set_xlabel("Periodo Estructural T (s)", fontsize=12)
        ax.set_ylabel("Pseudo-Aceleración Sa (cm/s²)", fontsize=12)
        
        ax.legend()
        ax.grid(True, linestyle='--', alpha=0.7)
        plt.tight_layout()
        self._guardar_figura(fig, "grafica_3.png")

    # =========================================================================
    # MÓDULO 4: ESPECTRO OBJETIVO Y ESCALAMIENTO POR MÍNIMOS CUADRADOS
    # =========================================================================
    def generar_espectro_objetivo_y_escalar(self, zona=3, uso='A', suelo='S1', R=2.0, t_max=5.0, paso=0.02):
        if self.espectros.empty: return

        print("\n" + "="*50)
        print("INICIANDO MÓDULO 4: ESPECTRO OBJETIVO Y ESCALAMIENTO")
        print("="*50)

        zona = int(zona)
        uso = str(uso).upper().strip()
        suelo = str(suelo).upper().strip()
        R = float(R)

        self.parametros_normativos = {
            "zona": zona,
            "uso": uso,
            "suelo": suelo,
            "R": R,
            "t_max": t_max,
            "paso": paso,
        }

        if "Periodo (T)" in self.espectros.columns:
            self.espectros = self.espectros[self.espectros["Periodo (T)"] <= t_max].copy().reset_index(drop=True)

        Z_dict = {4: 0.45, 3: 0.35, 2: 0.25, 1: 0.10}
        U_dict = {'A': 1.5, 'B': 1.3, 'C': 1.0}
        S_dict = {
            4: {'S0': 0.80, 'S1': 1.00, 'S2': 1.05, 'S3': 1.10},
            3: {'S0': 0.80, 'S1': 1.00, 'S2': 1.15, 'S3': 1.20},
            2: {'S0': 0.80, 'S1': 1.00, 'S2': 1.20, 'S3': 1.40},
            1: {'S0': 0.80, 'S1': 1.00, 'S2': 1.60, 'S3': 2.00}
        }
        T_dict = {
            'S0': {'Tp': 0.3, 'Tl': 3.0},
            'S1': {'Tp': 0.4, 'Tl': 2.5},
            'S2': {'Tp': 0.6, 'Tl': 2.0},  
            'S3': {'Tp': 1.0, 'Tl': 1.6}   
        }

        Z = Z_dict.get(zona, 0.45)
        U = U_dict.get(uso, 1.0)
        S = S_dict.get(zona, {}).get(suelo, 1.0)
        Tp = T_dict.get(suelo, {}).get('Tp', 0.4)
        Tl = T_dict.get(suelo, {}).get('Tl', 2.5)
        g = 981.0

        print(f"Parametros Normativos: zona={zona}, uso={uso}, suelo={suelo}, R={R}, Z={Z}, U={U}, S={S}, Tp={Tp}s, Tl={Tl}s")

        # Construcción del Espectro Objetivo Normativo
        sa_objetivo = []
        for T in self.espectros["Periodo (T)"]:
            if T < 0.2 * Tp:
                C = 1 + 7.5 * (T / Tp)
            elif 0.2 * Tp <= T <= Tp:
                C = 2.5
            elif Tp < T < Tl:
                C = 2.5 * (Tp / T)
            else:
                C = 2.5 * ((Tp * Tl) / (T**2))

            sa = (Z * U * C * S * g) / R
            sa_objetivo.append(sa)

        self.espectros['Sa_Norma(cm/s²)'] = np.array(sa_objetivo)

        # CÁLCULO DEL FACTOR DE ESCALA (MÉTODOS DE MÍNIMOS CUADRADOS)
        sa_srss = self.espectros['Sa_SRSS(cm/s²)'].values
        sa_norma = self.espectros['Sa_Norma(cm/s²)'].values
        
        # Minimiza la diferencia de áreas para acomodar la curva a la norma
        SF = np.sum(sa_srss * sa_norma) / np.sum(sa_srss**2)

        print(f"Factor de Escala (SF) optimizado por Mínimos Cuadrados: {SF:.4f}")

        # Escalamiento
        for comp in [self.componente_ew, self.componente_ns, self.componente_ud]:
            self.datos[f"{comp}_Escalado"] = self.datos[f"{comp}_Filt"] * SF
            self.espectros[f"Sa_{comp}_Escalado(cm/s²)"] = self.espectros[f"Sa_{comp}(cm/s²)"] * SF

        self.espectros['Sa_SRSS_Escalado(cm/s²)'] = self.espectros['Sa_SRSS(cm/s²)'] * SF
        self.sf_calculado = SF
        print("Espectro acomodado a la norma exitosamente.")

    def graficar_comparativa_escalamiento(self):
        # Gráfica 4: Comparativa Final
        if 'Sa_Norma(cm/s²)' not in self.espectros.columns: return

        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(self.espectros["Periodo (T)"], self.espectros["Sa_SRSS(cm/s²)"], color='gray', linestyle='--', label='Original: SRSS Filtrado (Sin escalar)', linewidth=1.5)
        ax.plot(self.espectros["Periodo (T)"], self.espectros["Sa_SRSS_Escalado(cm/s²)"], color='red', label=f'Escalado (Acomodado) SF: {self.sf_calculado:.2f}', linewidth=2)
        ax.plot(self.espectros["Periodo (T)"], self.espectros["Sa_Norma(cm/s²)"], color='blue', label='Objetivo: Z U C S * g / R', linewidth=2.5)

        zona = self.parametros_normativos.get("zona", "N/D")
        uso = self.parametros_normativos.get("uso", "N/D")
        suelo = self.parametros_normativos.get("suelo", "N/D")
        R = self.parametros_normativos.get("R", "N/D")
        ax.set_title(f"4. Compatibilización Sísmica: Z={zona} | Uso={uso} | Suelo={suelo} | R={R}", fontsize=14, weight='bold')
        ax.set_xlabel("Periodo Estructural T (s)", fontsize=12)
        ax.set_ylabel("Pseudo-Aceleración Sa (cm/s²)", fontsize=12)
        
        ax.set_xlim([0, 5.0])
        ax.legend(loc='upper right')
        ax.grid(True, linestyle='--', alpha=0.7)
        plt.tight_layout()
        self._guardar_figura(fig, "grafica_4.png")

# ==========================================
# EJECUCIÓN DIRECTA
# ==========================================
if __name__ == "__main__":
    print("Iniciando análisis de registro sísmico...")
    
    archivo = "loreto.txt"  
    registro = RegistroSismico()
    
    print(f"Cargando archivo: {archivo}")
    registro.cargar_txt(archivo)

    if not registro.datos.empty:
        print(f"Archivo cargado: {len(registro.datos)} registros")
        # Modulo 1
        registro.ejecutar_eda_completo()
        
        # Modulo 2
        registro.procesar_linea_base_y_filtrado(f_low=0.1, f_high=25.0, orden=4)
        registro.graficar_todas_filtradas()
        
        # Modulo 3
        registro.generar_espectros(amortiguamiento=0.05, t_max=5.0, paso=0.02)
        registro.graficar_espectros()
        
        # Modulo 4
        registro.generar_espectro_objetivo_y_escalar(
            zona=PARAMETROS_NORMATIVOS["zona"],
            uso=PARAMETROS_NORMATIVOS["uso"],
            suelo=PARAMETROS_NORMATIVOS["suelo"],
            R=PARAMETROS_NORMATIVOS["R"],
            t_max=5.0,
            paso=0.02,
        )
        registro.graficar_comparativa_escalamiento()

        output_dir = os.path.abspath(os.path.dirname(__file__))
        print(f"\nGráficas guardadas en: {output_dir}")
