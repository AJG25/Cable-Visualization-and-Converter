# Cable-Visualization-and-Converter

A full-stack web application designed to support the **International Cable Protection Committee (ICPC)** in transitioning submarine cable data to the **S-100 electronic nautical chart standard**.

This tool enables:

- Map-based visualization of marine boundaries and submarine cables  
- Semi-automated conversion of inconsistent **KML/XLSX files** into S-100-compliant GeoJSON  
- Cable crossing detection and stakeholder notifications  
- Role-based user access for secure operations  

---

## Key Features

- **Interactive Map Dashboard** with five global maritime boundary layers  
- **File Converter**: Rule-based KML and Excel parser with DMS support and metadata validation  
- **Real-time Cable Crossing Alerts** using spatial intersection detection  
- **Secure User Login System** with personalized access and data privacy  
- **Performance Optimization** using vector tiles + GeoJSON hybrid architecture  

---

## Architecture & Tech Stack

### Backend
- `Python 3.10`, `Flask 3.1.0` (modular micro-framework)  
- `SQLite3` (lightweight geospatial DB for cables, users, boundaries)  
- `GeoPandas`, `Shapely`, `pyproj` for geospatial analytics and geometry validation  

### Converter Engine
- Rule-based extraction of coordinates and metadata from:
  - **Inconsistent XLSX files** (nested, unlabeled, or irregular formats)
  - **Structured KML files** (via Placemark parsing)
- Converts to **GeoJSON with S-100-compliant structure**
- Manual review/edit interface for user validation before saving or downloading  

### Frontend
- `HTML`, `CSS`, `JavaScript`, `Leaflet.js` for interactive map and UI  
- User dashboard for:
  - Marine zone overlays  
  - Cable route visualization  
  - Metadata editing  
  - Cable crossing notifications  

### Visualization / Mapping
- Dockerized `TileServer-GL` hosted on **Render**  
- Vector tiles generated using `Tippecanoe`  
- Basemap layers: **OpenStreetMap** and **ArcGIS Satellite Imagery**  

---

## Future Improvements

- Cloud deployment for scalable multi-user access  
- Full S-100 encoding support with direct export to IHO systems  
- Smarter metadata suggestions using LLMs  
- Enhanced audit trail for cable data modifications  
- Internationalized UI (multi-language support)  

---
