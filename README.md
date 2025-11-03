# 🔒 Análisis de Clustering Forense - Ciberataques

Proyecto de análisis forense para determinar si los ciberataques registrados provienen de 2 o 3 atacantes distintos utilizando técnicas de Machine Learning y clustering.

## 📋 Descripción del Proyecto

Este proyecto utiliza PySpark MLlib para realizar un análisis exhaustivo de clustering sobre datos de ciberataques. El objetivo principal es identificar patrones de comportamiento que permitan determinar cuántos atacantes distintos están detrás de los incidentes registrados.

### Características Principales

- **Análisis Exploratorio de Datos (EDA)** completo con visualizaciones
- **Clustering con K-Means y GMM** (Gaussian Mixture Models)
- **Validación con múltiples métricas**: Silhouette Score, ARI, BIC
- **Ingeniería de características** (ratios por minuto)
- **Reducción dimensional con PCA** para visualización
- **Dashboard interactivo** con Streamlit
- **Visualización geográfica** de ataques

## 🛠️ Requisitos

### Entorno de Desarrollo

- **Python**: 3.13.5
- **Gestor de paquetes**: Conda (recomendado)

### Dependencias Principales

```
- pyspark 4.0.1
- pandas
- numpy
- matplotlib
- seaborn
- plotly
- scikit-learn
- streamlit
- reportlab
```

## 📦 Instalación

### 1. Clonar el Repositorio

```powershell
git clone https://github.com/Rodrimansidub14/ConsultingHacking.git
cd ConsultingHacking
```

### 2. Crear el Entorno Conda

```powershell
conda env create -f environment.yml
```

O crear manualmente:

```powershell
conda create -n py-3.13.5 python=3.13.5
conda activate py-3.13.5
```

### 3. Instalar Dependencias

Si creaste el entorno manualmente:

```powershell
conda install numpy pandas matplotlib seaborn reportlab
pip install pyspark plotly streamlit scikit-learn
```

## 🚀 Ejecución del Proyecto

### Análisis en Jupyter Notebook

1. **Activar el entorno**:
   ```powershell
   conda activate py-3.13.5
   ```

2. **Abrir el notebook**:
   ```powershell
   jupyter notebook ConsultingNB.ipynb
   ```
   O simplemente abrir el archivo en VS Code.

3. **Ejecutar las celdas en orden** para:
   - Cargar y explorar los datos
   - Realizar feature engineering
   - Entrenar modelos de clustering
   - Generar visualizaciones
   - Exportar resultados a `data/hack_data_clustered.csv`

### Dashboard Interactivo

1. **Asegurarse de que el archivo de datos procesados existe**:
   - El notebook debe haber exportado `data/hack_data_clustered.csv`

2. **Activar el entorno** (si no está activo):
   ```powershell
   conda activate py-3.13.5
   ```

3. **Ejecutar el dashboard**:
   ```powershell
   streamlit run dashboard.py
   ```

4. **Acceder al dashboard**:
   - Abre tu navegador en: `http://localhost:8501`

### Páginas del Dashboard

El dashboard incluye 5 secciones principales:

1. **📊 Resumen Ejecutivo**
   - Objetivo y conclusiones del análisis
   - KPIs principales (Silhouette Score, ARI, Balance)
   - Visualización PCA de separación de clusters

2. **📈 Análisis Detallado**
   - Boxplots interactivos por métrica
   - Gráficos de dispersión con líneas de tendencia
   - Comparación de comportamiento entre clusters

3. **👥 Perfiles de Clústeres**
   - Estadísticas descriptivas por cluster
   - Histogramas y violin plots
   - Comparación de distribuciones

4. **🌍 Distribución Geográfica**
   - Mapa interactivo de ataques por ubicación
   - Tamaño de burbujas según frecuencia de ataques
   - Top 10 ubicaciones por cluster
   - Métricas geográficas

5. **🔧 Detalles Técnicos**
   - Vista de datos procesados
   - Descarga de resultados en CSV
   - Metodología completa

## 📊 Estructura del Proyecto

```
ConsultingHacking/
│
├── ConsultingNB.ipynb          # Notebook principal con análisis completo
├── dashboard.py                # Aplicación Streamlit
├── environment.yml             # Especificación del entorno conda
├── README.md                   # Este archivo
│
└── data/
    ├── hack_data.csv           # Datos originales
    └── hack_data_clustered.csv # Datos procesados con clusters (generado)
```

## 📈 Resultados Principales

### Conclusión del Análisis

✅ **El análisis confirma la presencia de DOS (2) atacantes distintos**

### Métricas de Validación

- **Silhouette Score**: 0.8176 (separación excelente)
- **Adjusted Rand Index (ARI)**: 1.000 (estabilidad perfecta)
- **Balance de Clusters**: 167/167 (perfectamente balanceado)
- **BIC (GMM)**: Favorece K=2 sobre K=3

### Diferencias entre Clusters

Los dos atacantes presentan comportamientos claramente diferenciados en:

- **Duración de sesión**: Cluster 0 (sesiones cortas) vs Cluster 1 (sesiones largas)
- **Transferencia de datos**: Patrones de volumen opuestos
- **Velocidad de tecleo (WPM)**: Estilos de digitación distintos
- **Servidores comprometidos**: Estrategias de ataque diferentes
- **Uso de Kali Linux**: Preferencias de herramientas distintas

## 🔍 Metodología

1. **Carga y Limpieza de Datos**
   - Lectura con PySpark
   - Normalización de nombres de columnas
   - Manejo de valores nulos

2. **Feature Engineering**
   - Creación de ratios por minuto:
     - `bytes_per_min`
     - `pages_per_min`
     - `servers_per_min`

3. **Clustering**
   - Normalización con StandardScaler
   - K-Means con método del codo
   - GMM con validación BIC
   - Bootstrap para estabilidad

4. **Validación**
   - Silhouette Score
   - Adjusted Rand Index
   - Análisis de balance de clusters

5. **Visualización**
   - PCA para reducción dimensional
   - Visualizaciones geográficas
   - Dashboard interactivo

## 🐛 Solución de Problemas

### Error: "ModuleNotFoundError: No module named 'plotly'"

```powershell
conda activate py-3.13.5
pip install plotly
```

### Error: "FileNotFoundError: data/hack_data_clustered.csv"

Ejecuta primero el notebook completo para generar el archivo de datos procesados.

### Error: Kernel restart en Jupyter

Reinstala las dependencias:
```powershell
conda activate py-3.13.5
pip install --force-reinstall pyspark
```

### Dashboard no se actualiza

Detén el servidor (Ctrl+C) y reinicia:
```powershell
streamlit run dashboard.py
```

## 📝 Notas Importantes

- **PySpark en Windows**: El proyecto utiliza `.toPandas()` en lugar de operaciones RDD para evitar problemas de conexión de workers en Windows con Python 3.13
- **Memoria**: PySpark puede requerir memoria considerable. Se recomienda al menos 8GB de RAM
- **Datos**: El archivo `hack_data.csv` debe estar en la carpeta `data/` antes de ejecutar el notebook

## 👨‍💻 Autor

**Rodrigo Mansilla**
- GitHub: [@Rodrimansidub14](https://github.com/Rodrimansidub14)

## 📄 Licencia

Este proyecto es de uso académico y de investigación.

---

**Última actualización**: Noviembre 2, 2025

Para preguntas o problemas, abrir un issue en el repositorio de GitHub.
