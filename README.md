# Vectra

**Vectra** is a high-performance, API-key-based vector database designed for fast and meaningful semantic search.
It enables users to generate embeddings, store vectors, and perform similarity searches using natural language queries without relying on traditional SQL-style filtering.

Vectra is built for developers who want **semantic understanding**, **speed**, and **control** over their vector data.

---

## 🚀 What is Vectra?

Vectra is a self-hosted vector database system that:

* Uses **HNSW (Hierarchical Navigable Small World)** graphs for fast vector similarity search
* Generates embeddings using a **lightweight local embedding model**
* Allows users to:

  * Register and generate an **API key**
  * Create and manage their **own vectors**
  * Perform **semantic search** via API endpoints
* Returns either:

  * The **stored object itself**, or
  * The **object ID**, allowing integration with the user’s own database

The goal is to provide **much faster and more semantically accurate search** compared to traditional SQL `LIKE` or rule-based filtering queries.

---

## 🧠 Why Semantic Search?

Traditional queries struggle with meaning.

Example:

> **Query:**
> `"Hourly wage not less than $13"`

With classic SQL, this requires rigid filters and predefined conditions.
With Vectra, the same query is converted into a vector and matched semantically against stored data, returning the correct results **without explicit field-based filtering**.

This approach is:

* More flexible
* More expressive
* Often significantly faster on large datasets

Vectra has been tested with **large, separate datasets**, consistently outperforming traditional querying approaches in both speed and relevance.

---
## 🌐 API-First Architecture & Vision

Vectra is intentionally designed as an **API-key–based service**, not as an in-process library.

The core idea behind this approach is simple:

> **All vector operations should happen outside the main application.**

Currently, all major operations are handled through a **small set of HTTP endpoints**, allowing applications to interact with Vectra using simple HTTP requests.

This design enables:

* Centralized vector creation
* Centralized semantic search
* Reduced computational load on main applications
* Language-agnostic integration (any app that can send HTTP requests)

---

### 🔁 Endpoint-Centered Workflow

At its core, Vectra is built around **three fundamental operations**:

1. **Vector creation (embedding generation)**
2. **Vector storage / indexing**
3. **Semantic search**

All interactions happen through **API endpoints**, authenticated via an `API_KEY`.

This means any application can:

* Send raw data to Vectra
* Let Vectra generate vectors
* Query semantic meaning later without embedding logic in the main app

The long-term goal is to deploy Vectra as a **standalone vector service** that can be consumed by:

* Single applications
* Multiple independent applications
* External clients

All without increasing the load or complexity of the main systems.

---

### 🧱 Toward Multi-Tenant & Scalable Usage

While the current implementation is still evolving, the architectural vision includes:

* Proper **multi-tenant support**
* User-specific vector isolation
* Optimized and configurable index management
* More advanced `API_KEY`-based authorization strategies

In future iterations, this system could evolve into:

* A more complex, optimized API-key-based platform
* A **microservices-oriented architecture**
* Or even **distributed vector generation and search services**, where:

  * Embedding generation
  * Indexing
  * Searching
    are deployed independently and scaled separately

This would allow Vectra to handle significantly larger workloads and concurrent usage scenarios.

---

### 🧠 Demonstrating Real-World Value

One of the motivations behind keeping Vectra simple at its core is to demonstrate **how powerful vector databases can be even in minimal form**.

To showcase this, a **sector-specific, AI-integrated project built on top of Vectra** is currently under development.

This upcoming project aims to demonstrate:

* Practical, real-world semantic search use cases
* Deep AI integration powered by Vectra’s vector infrastructure
* How meaningful results can be achieved without complex rule-based querying

> 🚧 **Under development**
> A real, production-oriented project powered by Vectra is coming soon.
> It will be added here once ready.

---

**Coming soon.**


## 🔑 Authentication Model

Vectra uses an **API key–based authentication system**.

Flow:

1. User registers
2. An API key is generated
3. All vector-related operations are performed using this API key
4. Each user logically owns their vectors and searches

> ⚠️ Note:
> User-specific index isolation and index storage strategies are still under active development.

---

## 🧩 Core Features

* 🔐 API-key-based access
* 🧬 Local embedding generation (no external API dependency)
* ⚡ HNSW-powered similarity search
* 📦 Object or ID-based search results
* 🧠 Natural language semantic querying
* 🏎️ Optimized for speed and relevance

---

## 🛠️ Current Limitations (Work in Progress)

Vectra is **not production-ready yet**.
Some important features are still missing or incomplete:

* ❌ Per-user isolated index files
* ❌ Proper index classification and storage strategy
* ❌ Production-grade deployment setup
* ❌ Public API access & rate limiting
* ❌ Persistence and lifecycle management for indexes

These are planned improvements.

---

## 🗺️ Roadmap

Planned next steps include:

* User-specific index creation and isolation
* Configurable index storage paths
* Improved index metadata management
* Deployment-ready configuration
* API usage limits and monitoring
* Better documentation and usage examples

---

## 🧪 Tech Stack

* **Python**
* **HNSW** for vector similarity search
* **Local embedding model**
* Custom API layer
* File-based index storage (for now)

---

## 📌 Project Status

Vectra is currently a **research and development project** focused on:

* Exploring fast semantic search
* Evaluating vector-based querying over traditional databases
* Building a flexible, developer-friendly vector database API

It is actively evolving and not yet open for public production use.

---

## 🤝 Contributing

Contributions, discussions, and ideas are welcome.
This project is still experimental, so feedback is highly valuable.

---

## 📜 License

License information will be added.

---

**Vectra**
Fast, semantic, and developer-controlled vector search.


tahsinkocw@gmail.com
