document.addEventListener("DOMContentLoaded", () => {
  const dropArea = document.getElementById("drop-area");
  const fileInput = document.getElementById("fileInput");
  const originalImagePreview = document.getElementById(
    "original-image-preview"
  );
  const resultImage = document.getElementById("result-image");
  const downloadBtn = document.getElementById("download-btn");
  const processBtn = document.getElementById("process-btn");

  let uploadedFile = null;

  // Handle drag and drop and file input events
  dropArea.addEventListener("click", () => fileInput.click());
  fileInput.addEventListener("change", (event) => {
    const files = event.target.files;
    if (files.length > 0) {
      handleFiles(files);
    }
  });

  ["dragenter", "dragover", "dragleave", "drop"].forEach((eventName) => {
    dropArea.addEventListener(eventName, preventDefaults, false);
  });

  ["dragenter", "dragover"].forEach((eventName) => {
    dropArea.addEventListener(
      eventName,
      () => dropArea.classList.add("border-blue-400"),
      false
    );
  });

  ["dragleave", "drop"].forEach((eventName) => {
    dropArea.addEventListener(
      eventName,
      () => dropArea.classList.remove("border-blue-400"),
      false
    );
  });

  dropArea.addEventListener(
    "drop",
    (event) => {
      const dt = event.dataTransfer;
      const files = dt.files;
      handleFiles(files);
    },
    false
  );

  function preventDefaults(e) {
    e.preventDefault();
    e.stopPropagation();
  }

  function handleFiles(files) {
    uploadedFile = files[0];
    if (uploadedFile.type.startsWith("image/")) {
      const reader = new FileReader();
      reader.onload = (e) => {
        originalImagePreview.src = e.target.result;
        originalImagePreview.classList.remove("hidden");
        dropArea.classList.add("hidden");
        processBtn.disabled = false;
        resultImage.src = "";
        downloadBtn.style.display = "none";
      };
      reader.readAsDataURL(uploadedFile);
    } else {
      alert("Veuillez déposer une image valide.");
      uploadedFile = null;
    }
  }

  // Process the image
  processBtn.addEventListener("click", async () => {
    if (!uploadedFile) {
      alert("Veuillez d'abord télécharger une image.");
      return;
    }

    processBtn.textContent = "Traitement en cours...";
    processBtn.disabled = true;

    const formData = new FormData();
    formData.append("file", uploadedFile);

    try {
      const response = await fetch("/remove-bg/", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const blob = await response.blob();
      const imageUrl = URL.createObjectURL(blob);

      resultImage.src = imageUrl;
      downloadBtn.href = imageUrl;
      downloadBtn.download = `chromakey-result-${Date.now()}.png`;
      downloadBtn.style.display = "block";
    } catch (error) {
      console.error("Erreur lors de la suppression de l'arrière-plan:", error);
      alert(
        "Une erreur est survenue lors du traitement de l'image. Veuillez vérifier la console."
      );
    } finally {
      processBtn.textContent = "Supprimer l'arrière-plan";
      processBtn.disabled = false;
    }
  });
});
