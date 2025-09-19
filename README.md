### 🎨 **ChromaKey**

Salut \! 👋 Bienvenue sur **ChromaKey** — l'outil web open-source qui supprime l'arrière-plan de vos images en un clin d'œil. Oubliez les découpes manuelles fastidieuses \! Notre application utilise une **API externe ultra-puissante** pour vous garantir une qualité de découpe professionnelle, même pour les logos, les portraits ou les objets les plus complexes.

**🚀 Prêt à transformer vos images ?**

---

### ✨ **Points Forts**

- 🖼️ **Qualité Premium** : Fini les découpes floues \! On s'appuie sur une API tierce pour un résultat impeccable.
- 🖱️ **Glisser-Déposer** : Un geste simple pour un résultat magique.
- 🔄 **Réinitialisation Instantanée** : Un bouton pour repartir de zéro sans recharger la page.
- ⚡ **Rapide et Fluide** : Une interface utilisateur pensée pour une expérience sans accroc.
- 📂 **Open Source** : Le code est ouvert, et on adore les contributions \!

---

### 🛠️ **Technologies Utilisées**

Ce projet est une démonstration de ce qu'on peut faire avec des outils modernes et une API.

- **Backend (Python)**

  - **FastAPI** : Le framework web star, pour un développement rapide et performant.
  - **Requests** : Notre allié pour communiquer avec l'API de suppression de fond.

- **Frontend (Web)**

  - **HTML & JavaScript** : La base de notre interface interactive.
  - **Tailwind CSS** : Pour un design épuré, stylé et entièrement personnalisable.

---

### 🏃 **Lancement en 3 Étapes**

**1. Clonez le projet :**

```bash
git clone git@github.com:ranto-dev/ChromaKey.git
cd ChromaKey
```

**2. Installez les dépendances :**

```bash
pip install -r requirements.txt
```

_Note : Nous recommandons l'utilisation d'un environnement virtuel (venv)._

**3. Configurez votre clé API :**
Pour utiliser le service externe, vous aurez besoin d'une clé API. Une fois que vous l'avez, configurez-la comme variable d'environnement (méthode recommandée) :

```bash
export REMBG_API_KEY="votre_clé_api"
```

Puis lancez le serveur :

```bash
uvicorn main:app --reload
```

Votre application est maintenant accessible sur **`http://127.0.0.1:8000`**.

---

### 🙏 **Contributions**

Ce projet est fait avec passion, et on serait ravis de vous voir le faire grandir \! Que ce soit pour un rapport de bug, une nouvelle fonctionnalité ou une simple idée, n'hésitez pas à ouvrir une **issue** ou à soumettre une **pull request**.
