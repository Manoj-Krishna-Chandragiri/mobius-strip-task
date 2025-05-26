# Möbius Strip Modeling in Python

## 👤 Author
**Manoj Krishna Chandragiri**
- GitHub: [@Manoj-Krishna-Chandragiri](https://github.com/Manoj-Krishna-Chandragiri)

## 📌 Task Description
This script models a Möbius strip using parametric equations, computes the surface area and edge length numerically, and visualizes the 3D surface.

## 🧱 Code Structure

- **Class:** `MobiusStrip` – Handles mesh generation, surface area and edge length calculations, and plotting.
- **Functions:**
  - `generate_mesh()` – Generates X, Y, Z coordinates.
  - `compute_surface_area()` – Estimates area using cross product of partial derivatives.
  - `compute_edge_length()` – Calculates boundary length numerically.
  - `plot()` – Renders a 3D surface using matplotlib.

## 📐 Surface Area Calculation

The surface area is computed by:
- Taking gradients of X, Y, Z in u and v directions.
- Computing the cross product to get the local area element.
- Summing all elements and multiplying by step size in u and v.

## 📏 Edge Length Calculation

Edge points along v = w/2 are extracted, and distances between them are calculated using Euclidean norm.

## 🎯 Challenges Faced

- Ensuring numerical stability in gradient calculations.
- Handling the twisted topology of the Möbius strip for correct visualization.
- Selecting a fine enough resolution `n` to maintain visual and numerical accuracy.

## 📊 Output

- Surface Area: 0.0001
- Edge Length: 6.3316
- See `output.png` for visualization.

## ✅ Requirements
Python 3.7+ with NumPy and Matplotlib installed

