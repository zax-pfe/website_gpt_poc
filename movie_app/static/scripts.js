// Custom JavaScript

// Animate the title
// const title = document.querySelector(".title");
// title.animate([
//     { transform: "translateY(-100%)" },
//     { transform: "translateY(0)" }
// ], {
//     duration: 1000,
//     easing: "ease-out"
// });

// Add hover effect to table rows
const tableRows = document.querySelectorAll(".result-row");
tableRows.forEach(row => {
    row.addEventListener("mouseover", () => {
        row.style.backgroundColor = "#f1f1f1";
    });

    row.addEventListener("mouseout", () => {
        row.style.backgroundColor = "";
    });
});

// Show loading spinner on form submit
const form = document.querySelector("#search-form");
const loading = document.querySelector("#loading");
form.addEventListener("submit", (e) => {
    loading.style.display = "flex";
});

// Add your other animations and effects here