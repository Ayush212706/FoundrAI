document.addEventListener("DOMContentLoaded", () => {

    console.log("FoundrAI Dashboard Loaded");

    // -----------------------------
    // Founder Skills Radar Chart
    // -----------------------------

    const chartCanvas = document.getElementById("skillsChart");

    if (chartCanvas && window.founderData) {

        new Chart(chartCanvas, {

            type: "radar",

            data: {

                labels: [
                    "Programming",
                    "Marketing",
                    "Finance",
                    "Leadership",
                    "Communication",
                    "Problem Solving",
                    "Risk"
                ],

                datasets: [{

                    label: "Founder Skills",

                    data: [

                        Number(window.founderData.programming) || 0,
                        Number(window.founderData.marketing) || 0,
                        Number(window.founderData.finance) || 0,
                        Number(window.founderData.leadership) || 0,
                        Number(window.founderData.communication) || 0,
                        Number(window.founderData.problem_solving) || 0,
                        Number(window.founderData.risk) || 0

                    ],

                    fill: true,

                    backgroundColor: "rgba(59,130,246,0.20)",

                    borderColor: "#3b82f6",

                    borderWidth: 2,

                    pointBackgroundColor: "#60a5fa",

                    pointBorderColor: "#ffffff",

                    pointHoverRadius: 6

                }]

            },

            options: {

                responsive: true,

                maintainAspectRatio: false,

                plugins: {

                    legend: {

                        labels: {

                            color: "#ffffff",

                            font: {

                                size: 14

                            }

                        }

                    }

                },

                scales: {

                    r: {

                        min: 0,

                        max: 10,

                        ticks: {

                            stepSize: 2,

                            color: "#cbd5e1",

                            backdropColor: "transparent"

                        },

                        angleLines: {

                            color: "#334155"

                        },

                        grid: {

                            color: "#334155"

                        },

                        pointLabels: {

                            color: "#ffffff",

                            font: {

                                size: 13,

                                weight: "bold"

                            }

                        }

                    }

                }

            }

        });

    }

    // -----------------------------
    // Card Hover Effect
    // -----------------------------

    document.querySelectorAll(".card").forEach(card => {

        card.addEventListener("mouseenter", () => {

            card.style.transform = "translateY(-6px)";

        });

        card.addEventListener("mouseleave", () => {

            card.style.transform = "translateY(0px)";

        });

    });

    // -----------------------------
    // Button Ripple
    // -----------------------------

    document.querySelectorAll(".btn").forEach(button => {

        button.addEventListener("click", () => {

            button.style.opacity = "0.85";

            setTimeout(() => {

                button.style.opacity = "1";

            }, 150);

        });

    });

    // -----------------------------
    // Animate Progress Bars
    // -----------------------------

    document.querySelectorAll(".progress-bar").forEach(bar => {

        const width = bar.getAttribute("aria-valuenow") || "0";

        bar.style.width = "0%";

        setTimeout(() => {

            bar.style.width = width + "%";

        }, 300);

    });

    // -----------------------------
    // Auto Hide Alerts
    // -----------------------------

    document.querySelectorAll(".alert").forEach(alert => {

        setTimeout(() => {

            alert.classList.add("fade");

        }, 5000);

    });

    // -----------------------------
    // Dashboard Statistics
    // -----------------------------

    const cards = document.querySelectorAll(".stat-card");

    cards.forEach(card => {

        card.addEventListener("mouseenter", () => {

            card.style.transition = "0.3s";

            card.style.boxShadow = "0 0 20px rgba(59,130,246,0.35)";

        });

        card.addEventListener("mouseleave", () => {

            card.style.boxShadow = "";

        });

    });

    console.log("Dashboard Initialized Successfully");

});