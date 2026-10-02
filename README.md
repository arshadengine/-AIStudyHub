# AIStudyHub — AI & Data Science Student Resource Portal

A modern, comprehensive educational resource portal designed for Artificial Intelligence and Data Science engineering undergraduates.

**Live Website:** [https://arshadengine.github.io/-AIStudyHub/](https://arshadengine.github.io/-AIStudyHub/)  
**GitHub Repository:** [https://github.com/arshadengine/-AIStudyHub.git](https://github.com/arshadengine/-AIStudyHub.git)

---

## 📚 Features & Academic Content

### 1. Core Subject Portals
* **Artificial Intelligence (`ai.html`):** Rational agents, uninformed & heuristic search (BFS, DFS, A*), adversarial search (Minimax, Alpha-Beta pruning), propositional & First-Order Logic (FOL), and knowledge representation.
* **Machine Learning (`machine-learning.html`):** Supervised regression & classification, unsupervised clustering (K-Means, PCA), model evaluation (confusion matrix, precision/recall, ROC-AUC), and neural networks.
* **Data Science (`data-science.html`):** End-to-end data lifecycle, data cleaning & imputation, Exploratory Data Analysis (EDA), visualization, and inferential statistics.
* **Python for AI & DS (`python.html`):** Core syntax, OOP, NumPy vectorization, Pandas DataFrame manipulation, and lab cheat sheets.
* **Mathematics for AI (`mathematics.html`):** Linear algebra (vectors, eigenvalues, SVD), multivariate calculus (gradients, chain rule), probability distributions, Bayes' Theorem, and optimization algorithms with NumPy code snippets.

### 2. Comprehensive Study Material (`study-material.html`)
* Structured curriculum across all 5 core subject domains.
* Standard textbook references (Russell & Norvig, Bishop, Géron, McKinney, Strang).
* Semester-wise learning roadmap aligned with undergraduate engineering syllabi (Semesters 1 through 6).

### 3. Interactive Question Bank (`question-bank.html`)
* **Unit 1:** Foundations of AI, Problem Formulation, State Space & Heuristic Search
* **Unit 2:** Knowledge Representation, First-Order Logic & Resolution Refutation
* **Unit 3:** Supervised Learning, Decision Trees, Naive Bayes & Model Validation
* **Unit 4:** Neural Networks, Backpropagation, CNNs & AI Ethics / Algorithmic Bias
* **Previous Year Questions (PYQs):** University examination pattern analysis (2022–2024) with marks breakdown (2M / 5M / 10M) and interactive expandable model solutions (`<details>`/`<summary>`).

### 4. Featured Master Guide (`blog/ml-roadmap.html`)
* **"How to Start Learning Machine Learning: A Beginner's Roadmap for AI & Data Science Students"**
* 7-phase step-by-step roadmap from Python and mathematics to real-world deployment.
* Scikit-Learn reproducible code pipeline.
* 12-week semester study timeline, common student pitfalls, and curated learning resources.

### 5. Technical SEO & Web Standards
* Responsive, accessible layout with dark mode aesthetic accents.
* Semantic HTML5 elements and Open Graph tags on all pages.
* Canonical URLs pointing to `https://arshadengine.github.io/-AIStudyHub/`.
* Clean `sitemap.xml` and `robots.txt` for search engine indexing.

---

## 🚀 Running Locally
Simply open `index.html` in any web browser, or launch using VS Code Live Server or Python HTTP server:

```bash
# Using Python built-in server
python -m http.server 8000
# Open http://localhost:8000 in your browser
```

---

## 🌐 Deployment to GitHub Pages

1. Initialize repository and add remote:
   ```bash
   git init
   git remote add origin https://github.com/arshadengine/-AIStudyHub.git
   ```
2. Stage and commit:
   ```bash
   git add .
   git commit -m "feat: complete academic content and portal setup"
   ```
3. Push to `main` (or `master`):
   ```bash
   git branch -M main
   git push -u origin main
   ```
4. In GitHub, navigate to **Settings** → **Pages** → under **Build and deployment**, select **Deploy from a branch**, choose `main` branch and `/ (root)` folder, then save.
