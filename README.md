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
