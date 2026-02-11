## 🚀 Getting Started

**Electronic Shop - FlipKart-Recommender-RAG**

This is my working RAG system built around a real Flipkart dataset and a real deployment mindset with observability, API surface, and practical wiring!

## Tech Stack

**Backend**
- Python 3.10  
- Flask  

**RAG Pipeline**
- LangChain  
- HuggingFace Embedding model (llama-3.1-8b-instant) 
- Vector Store (ASTRA_DB)

**Data Processing**
- Pandas  
- NumPy  
- Flipkart product dataset  

**Observability**
- Prometheus (metrics scraping)  
- Grafana (dashboards) 

**Infrastructure**
- Docker  
- Kubernetes (minikube and kubectl)  
- GCP (VM instance, E2 at least 16 GB RAM and Ubuntu 24.04 LTS)

## Running the Application

```bash
### Install dependencies
git clone https://github.com/emanehabn/FlipKart-Recommender-RAG.git
cd FlipKart-Recommender-RAG
pip install -e .

python app.py

```
###  Environment Variables

Before running the project, make sure to **configure your keys** in a `.env` file.  

You can use `.env.example` as a template:

---

## 📸 & 🎥 Project Gallery

Check out the full system — API responses, metrics, dashboards, observability and a demo video.


### Gallery
👉 **[Click here](gallery/)**


### 🔹 Demo Video

<p align="center">
  <video width="800" controls>
    <source src="Gallery/demo.mp4" type="video/mp4">
      <em>Watch the flipkart responces.</em>
  </video>
</p>
