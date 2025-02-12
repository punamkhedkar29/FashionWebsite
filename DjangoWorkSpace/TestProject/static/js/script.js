function toggleFavorite(event, image, title, description) {
    event.preventDefault(); // Prevent link from navigating

    let heartIcon = event.currentTarget.querySelector("svg");
    let favorites = JSON.parse(localStorage.getItem("favorites")) || [];

    let existingIndex = favorites.findIndex(product => product.image === image);

    if (existingIndex !== -1) {
        favorites.splice(existingIndex, 1);
        heartIcon.style.fill = "black"; // Default color
    } else {
        favorites.push({ image, title, description });
        heartIcon.style.fill = "red"; // Turn heart red
    }

    localStorage.setItem("favorites", JSON.stringify(favorites));
}
