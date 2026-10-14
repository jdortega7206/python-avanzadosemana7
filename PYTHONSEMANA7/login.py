"""Interfaz de inicio de sesión con Tkinter.

Widgets utilizados:
- Label + Entry → Usuario / correo electrónico
- Entry (con show="") → Contraseña
- Checkbutton → Recordar sesión
- Button → Botones de acción (Ingresar, Olvidé mi contraseña)
- Message/Label → Mensajes de estado y validación

Justificación:
- El usuario es un dato corto alfanumérico → Entry con Label.
- La contraseña es sensible → Entry sin mostrar caracteres.
- Recordar sesión es una decisión binaria → Checkbutton.
- Las acciones del sistema se activan con Button.
"""

import tkinter as tk
from tkinter import messagebox


class LoginWindow:
    """Ventana de inicio de sesión."""

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Inicio de Sesión")
        self.root.geometry("400x350")
        self.root.resizable(False, False)

        # Configuración general del formulario
        self._configurar_estilo()
        self._crear_widgets()

    def _configurar_estilo(self) -> None:
        """Configura estilos básicos para una apariencia limpia."""
        self.root.configure(bg="#f0f2f5")

        style_font = ("Arial", 11, "normal")
        title_font = ("Arial", 16, "bold")

    def _crear_widgets(self) -> None:
        """Crea los widgets de la interfaz de login."""

        # --- Encabezado ---
        titulo_label = tk.Label(
            self.root,
            text="🔐 Inicio de Sesión",
            font=("Arial", 18, "bold"),
            bg="#f0f2f5",
            fg="#333"
        )
        titulo_label.pack(pady=40)

        # --- Contenedor del formulario ---
        frame_formulario = tk.Frame(self.root, bg="#ffffff", relief="raised", bd=1)
        frame_formulario.pack(padx=20, pady=10, fill="both", expand=True)

        # --- Campo: Usuario / Correo ---
        label_usuario = tk.Label(
            frame_formulario,
            text="Usuario o correo electrónico:",
            font=("Arial", 10),
            bg="#ffffff"
        )
        label_usuario.pack(pady=(5, 2))

        entry_usuario = tk.Entry(
            frame_formulario,
            width=30,
            font=("Arial", 10)
        )
        entry_usuario.pack(pady=(0, 10), fill="x")

        # --- Campo: Contraseña ---
        label_contrasena = tk.Label(
            frame_formulario,
            text="Contraseña:",
            font=("Arial", 10),
            bg="#ffffff"
        )
        label_contrasena.pack(pady=(5, 2))

        entry_contrasena = tk.Entry(
            frame_formulario,
            width=30,
            font=("Arial", 10),
            show="*"  # Oculta los caracteres para seguridad visual
        )
        entry_contrasena.pack(pady=(0, 10), fill="x")

        # --- Checkbutton: Recordar sesión ---
        self.check_remember = tk.Checkbutton(
            frame_formulario,
            text="📌 Recordar mi sesión",
            font=("Arial", 9)
        )
        self.check_remember.pack(pady=(5, 10))

        # --- Botones de acción ---
        frame_botones = tk.Frame(frame_formulario, bg="#ffffff")
        frame_botones.pack(fill="x", pady=10)

        btn_ingresar = tk.Button(
            frame_botones,
            text="🔓 Ingresar",
            command=self._ingresar,
            font=("Arial", 10, "bold"),
            bg="#4CAF50",
            fg="white",
            relief="raised",
            padx=20,
            pady=8
        )
        btn_ingresar.pack(side=tk.LEFT, padx=5)

        btn_olvide = tk.Button(
            frame_botones,
            text="📩 ¿Olvidé mi contraseña?",
            command=self._mostrar_mensaje_olvido,
            font=("Arial", 9),
            bg="#2196F3",
            fg="white",
            relief="flat",
            padx=5,
            pady=4
        )
        btn_olvide.pack(side=tk.LEFT, padx=5)

        # --- Mensaje de estado (validación/errores) ---
        self.mensaje_estado = tk.Label(
            frame_formulario,
            text="",
            font=("Arial", 9),
            bg="#ffffff"
        )
        self.mensaje_estado.pack(pady=(10, 5))

    def _ingresar(self) -> None:
        """Procesa el inicio de sesión."""
        usuario = entry_usuario.get() if (entry_usuario := self.root.master.winfo_children()[0].winfo_children()[0]) else ""
        contrasena = entry_contrasena.get()

        # Validación simple (simulada)
        if not usuario or not contrasena:
            self.mensaje_estado.config(
                text="⚠️ Error: Complete todos los campos.",
                fg="#d32f2f"
            )
            return

        messagebox.showinfo("Éxito", "Bienvenido al sistema.")

    def _mostrar_mensaje_olvido(self) -> None:
        """Muestra un mensaje de ayuda para recuperación de contraseña."""
        messagebox.showinfo(
            "Recuperación",
            "Si ha olvidado su contraseña, contacte al soporte técnico."
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = LoginWindow(root)
    root.mainloop()
