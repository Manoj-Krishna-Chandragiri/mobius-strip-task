import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class MobiusStrip:
    def __init__(self, R=1.0, w=0.3, n=100):
        self.R = R
        self.w = w
        self.n = n
        self.u = np.linspace(0, 2 * np.pi, n)
        self.v = np.linspace(-w / 2, w / 2, n)
        self.U, self.V = np.meshgrid(self.u, self.v)
        self.X, self.Y, self.Z = self.generate_mesh()

    def generate_mesh(self):
        u = self.U
        v = self.V
        R = self.R
        x = (R + v * np.cos(u / 2)) * np.cos(u)
        y = (R + v * np.cos(u / 2)) * np.sin(u)
        z = v * np.sin(u / 2)
        return x, y, z

    def compute_surface_area(self):
        du = 2 * np.pi / (self.n - 1)
        dv = self.w / (self.n - 1)
        Xu = np.gradient(self.X, axis=1)
        Yu = np.gradient(self.Y, axis=1)
        Zu = np.gradient(self.Z, axis=1)
        Xv = np.gradient(self.X, axis=0)
        Yv = np.gradient(self.Y, axis=0)
        Zv = np.gradient(self.Z, axis=0)
        cross_X = Yu * Zv - Zu * Yv
        cross_Y = Zu * Xv - Xu * Zv
        cross_Z = Xu * Yv - Yu * Xv
        dA = np.sqrt(cross_X**2 + cross_Y**2 + cross_Z**2)
        surface_area = np.sum(dA) * du * dv
        return surface_area

    def compute_edge_length(self):
        v = self.w / 2
        u_vals = self.u
        x = (self.R + v * np.cos(u_vals / 2)) * np.cos(u_vals)
        y = (self.R + v * np.cos(u_vals / 2)) * np.sin(u_vals)
        z = v * np.sin(u_vals / 2)
        dx = np.gradient(x)
        dy = np.gradient(y)
        dz = np.gradient(z)
        ds = np.sqrt(dx**2 + dy**2 + dz**2)
        edge_length = np.sum(ds)
        return edge_length

    def plot(self, save=False):
        fig = plt.figure(figsize=(10, 6))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(self.X, self.Y, self.Z, rstride=2, cstride=2, cmap='viridis', edgecolor='k', alpha=0.9)
        ax.set_title('Mobius Strip')
        plt.tight_layout()
        if save:
            plt.savefig("output.png") 
        plt.show()



strip = MobiusStrip(R=1.0, w=0.3, n=200)
area = strip.compute_surface_area()
edge = strip.compute_edge_length()
print(f"Surface Area: {area:.4f}")
print(f"Edge Length: {edge:.4f}")
strip.plot(save=True)
