"""Interfaz de registro de clientes con Tkinter.

Widgets utilizados:
- Label + Entry → Nombre completo, número de documento
- Combobox → Tipo de documento (DNI, Pasaporte, etc.)
- Radiobutton → Género (M/F/Otro)
- Checkbutton → Intereses / servicios de preferencia
- Combobox → Ciudad (selección de catálogo)
- Text → Observaciones adicionales
- Scale → Nivel de satisfacción o prioridad
- LabelFrame/Frame → Agrupación visual por secciones
- Message/Label → Mensajes de validación

Justificación:
- Cada widget responde al tipo de dato que debe capturarse.
- Los campos obligatorios se distinguen con un asterisco (*).
- La agrupación en secciones mejora la usabilidad y legibilidad.
"""

import tkinter as tk
from tkinter import messagebox, ttk


class RegistroWindow:
    """Ventana de registro de clientes."""

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Registro de Cliente")
        self.root.geometry("500x600")
        self.root.resizable(False, False)

        # Configuración general
        self._configurar_estilo()
        self._crear_widgets()

    def _configurar_estilo(self) -> None:
        """Configura estilos básicos."""
        self.root.configure(bg="#f5f7fa")

        style_font = ("Arial", 10, "normal")
        title_font = ("Arial", 16, "bold")
        label_font = ("Arial", 9)

    def _crear_widgets(self) -> None:
        """Crea los widgets de la interfaz de registro agrupados por secciones."""

        # --- Encabezado ---
        titulo_label = tk.Label(
            self.root,
            text="📋 Registro de Cliente",
            font=("Arial", 18, "bold"),
            bg="#f5f7fa",
            fg="#333"
        )
        titulo_label.pack(pady=20)

        # --- Sección: Datos Personales ---
        frame_personales = tk.LabelFrame(
            self.root,
            text="👤 Datos Personales",
            font=("Arial", 11, "bold"),
            padx=15,
            pady=10,
            bg="#f5f7fa"
        )
        frame_personales.pack(fill="both", expand=True, padx=20, pady=(0, 10))

        # Nombre completo
        label_nombre = tk.Label(
            frame_personales,
            text="Nombre completo:",
            font=label_font,
            bg="#f5f7fa"
        )
        label_nombre.pack(anchor=tk.W)

        entry_nombre = tk.Entry(frame_personales, width=30, font=("Arial", 10))
        entry_nombre.pack(fill="x", pady=(2, 8))

        # Tipo de documento (Combobox con lista cerrada)
        label_tipo_doc = tk.Label(
            frame_personales,
            text="Tipo de documento:",
            font=label_font,
            bg="#f5f7fa"
        )
        label_tipo_doc.pack(anchor=tk.W)

        self.combo_tipo_doc = ttk.Combobox(frame_personales, width=30, state="readonly")
        self.combo_tipo_doc["values"] = ["DNI", "Pasaporte", "Cédula", "Tarjeta de Identidad"]
        self.combo_tipo_doc.pack(fill="x", pady=(2, 8))

        # Número de documento (Entry numérico)
        label_num_doc = tk.Label(
            frame_personales,
            text="Número de documento:",
            font=label_font,
            bg="#f5f7fa"
        )
        label_num_doc.pack(anchor=tk.W)

        entry_num_doc = tk.Entry(frame_personales, width=30, font=("Arial", 10))
        entry_num_doc.pack(fill="x", pady=(2, 8))

        # Fecha de nacimiento (Entry con formato controlado)
        label_fecha_nac = tk.Label(
            frame_personales,
            text="Fecha de nacimiento:",
            font=label_font,
            bg="#f5f7fa"
        )
        label_fecha_nac.pack(anchor=tk.W)

        entry_fecha_nac = tk.Entry(frame_personales, width=30, font=("Arial", 10))
        entry_fecha_nac.pack(fill="x", pady=(2, 8))

        # Género (Radiobutton: solo una opción marcada)
        label_genero = tk.Label(
            frame_personales,
            text="Género:",
            font=label_font,
            bg="#f5f7fa"
        )
        label_genero.pack(anchor=tk.W)

        self.radio_genero_var = tk.StringVar(value="M")
        rb_masc = tk.Radiobutton(frame_personales, text="Masculino", variable=self.radio_genero_var, value="M")
        rb_masc.pack(anchor=tk.W)
        rb_fem = tk.Radiobutton(frame_personales, text="Femenino", variable=self.radio_genero_var, value="F")
        rb_fem.pack(anchor=tk.W)
        rb_otros = tk.Radiobutton(frame_personales, text="Otro", variable=self.radio_genero_var, value="O")
        rb_otros.pack(anchor=tk.W)

        # --- Sección: Contacto ---
        frame_contacto = tk.LabelFrame(
            self.root,
            text="📞 Datos de Contacto",
            font=("Arial", 11, "bold"),
            padx=15,
            pady=10,
            bg="#f5f7fa"
        )
        frame_contacto.pack(fill="both", expand=True, padx=20, pady=(0, 10))

        # Ciudad (Combobox con catálogo predefinido)
        label_ciudad = tk.Label(
            frame_contacto,
            text="Ciudad:",
            font=label_font,
            bg="#f5f7fa"
        )
        label_ciudad.pack(anchor=tk.W)

        self.combo_ciudad = ttk.Combobox(frame_contacto, width=30, state="readonly")
        self.combo_ciudad["values"] = ["Bogotá", "Medellín", "Cali", "Barranquilla", "Cartagena"]
        self.combo_ciudad.pack(fill="x", pady=(2, 8))

        # Dirección (Entry para texto de una línea)
        label_direccion = tk.Label(
            frame_contacto,
            text="Dirección:",
            font=label_font,
            bg="#f5f7fa"
        )
        label_direccion.pack(anchor=tk.W)

        entry_direccion = tk.Entry(frame_contacto, width=30, font=("Arial", 10))
        entry_direccion.pack(fill="x", pady=(2, 8))

        # --- Sección: Preferencias e Intereses ---
        frame_preferencias = tk.LabelFrame(
            self.root,
            text="📌 Preferencias e Intereses",
            font=("Arial", 11, "bold"),
            padx=15,
            pady=10,
            bg="#f5f7fa"
        )
        frame_preferencias.pack(fill="both", expand=True, padx=20, pady=(0, 10))

        # Intereses (Checkbutton: selección múltiple)
        label_intereses = tk.Label(
            frame_preferencias,
            text="Intereses:",
            font=label_font,
            bg="#f5f7fa"
        )
        label_intereses.pack(anchor=tk.W)

        self.check_interes1 = tk.Checkbutton(frame_preferencias, text="📱 Notificaciones por email")
        self.check_interes1.pack(anchor=tk.W, pady=2)
        self.check_interes2 = tk.Checkbutton(frame_preferencias, text="🔔 Recordatorios de sesión")
        self.check_interes2.pack(anchor=tk.W, pady=2)
        self.check_interes3 = tk.Checkbutton(frame_preferencias, text="📰 Boletín informativo")
        self.check_interes3.pack(anchor=tk.W, pady=2)

        # --- Sección: Observaciones ---
        frame_observaciones = tk.LabelFrame(
            self.root,
            text="📝 Observaciones Adicionales",
            font=("Arial", 11, "bold"),
            padx=15,
            pady=10,
            bg="#f5f7fa"
        )
        frame_observaciones.pack(fill="both", expand=True, padx=20, pady=(0, 10))

        # Text (para comentarios extensos)
        self.text_observaciones = tk.Text(
            frame_observaciones,
            height=5,
            width=40,
            font=("Arial", 9),
            bg="#fafafa"
        )
        self.text_observaciones.pack(fill="both", expand=True)

        # --- Sección: Validación y Mensajes de Estado ---
        frame_validacion = tk.LabelFrame(
            self.root,
            text="✅ Validación",
            font=("Arial", 11, "bold"),
            padx=15,
            pady=10,
            bg="#f5f7fa"
        )
        frame_validacion.pack(fill="both", expand=True, padx=20, pady=(0, 10))

        # Scale (para nivel de satisfacción o prioridad)
        label_prioridad = tk.Label(
            frame_validacion,
            text="Nivel de prioridad:",
            font=label_font,
            bg="#f5f7fa"
        )
        label_prioridad.pack(anchor=tk.W)

        self.scale_prioridad = tk.Scale(
            frame_validacion,
            from_=1,
            to=5,
            orient=tk.HORIZONTAL,
            length=200,
            font=("Arial", 9),
            bg="#f5f7fa"
        )
        self.scale_prioridad.pack(fill="x", pady=(2, 8))

        # Mensaje de estado (feedback visual)
        self.mensaje_estado = tk.Label(
            frame_validacion,
            text="",
            font=("Arial", 9),
            bg="#f5f7fa"
        )
        self.mensaje_estado.pack(pady=(2, 8))

        # --- Botones de acción ---
        frame_botones = tk.Frame(self.root, bg="#f5f7fa")
        frame_botones.pack(fill="x", padx=20, pady=10)

        btn_registrar = tk.Button(
            frame_botones,
            text="💾 Registrar Cliente",
            command=self._registrar,
            font=("Arial", 10, "bold"),
            bg="#4CAF50",
            fg="white",
            relief="raised",
            padx=20,
            pady=8
        )
        btn_registrar.pack(side=tk.LEFT, padx=5)

        btn_limpiar = tk.Button(
            frame_botones,
            text="🧹 Limpiar Formulario",
            command=self._limpiar,
            font=("Arial", 10),
            bg="#FF9800",
            fg="white",
            relief="raised",
            padx=20,
            pady=8
        )
        btn_limpiar.pack(side=tk.LEFT, padx=5)

        btn_cancelar = tk.Button(
            frame_botones,
            text="❌ Cancelar",
            command=self.root.quit,
            font=("Arial", 10),
            bg="#f44336",
            fg="white",
            relief="raised",
            padx=20,
            pady=8
        )
        btn_cancelar.pack(side=tk.LEFT, padx=5)

    def _registrar(self) -> None:
        """Procesa el registro del cliente."""
        nombre = entry_nombre.get() if (entry_nombre := self.root.master.winfo_children()[0].winfo_children()[0]) else ""
        tipo_doc = self.combo_tipo_doc.get()
        num_doc = entry_num_doc.get()

        # Validaciones simples
        errores = []

        if not nombre:
            errores.append("⚠️ El nombre completo es obligatorio.")
        if not tipo_doc:
            errores.append("⚠️ Seleccione un tipo de documento.")
        if not num_doc:
            errores.append("⚠️ Ingrese el número de documento.")

        if errores:
            self.mensaje_estado.config(text=" ".join(errores), fg="#d32f2f")
            messagebox.showwarning("Validación", "Por favor, corrija los campos marcados en rojo.")
            return

        messagebox.showinfo("Éxito", f"Cliente registrado con éxito.\nNombre: {nombre}\nDocumento: {num_doc}")

    def _limpiar(self) -> None:
        """Limpia todos los campos del formulario."""
        entry_nombre.delete(0, tk.END)
        self.combo_tipo_doc.current(0)
        entry_num_doc.delete(0, tk.END)
        entry_fecha_nac.delete(0, tk.END)
        self.radio_genero_var.set("M")
        self.combo_ciudad.current(0)
        entry_direccion.delete(0, tk.END)
        self.check_interes1.select()
        self.check_interes2.deselect()
        self.check_interes3.deselect()
        self.text_observaciones.delete("1.0", tk.END)
        self.scale_prioridad.set(5)
        self.mensaje_estado.config(text="", fg="#333")


if __name__ == "__main__":
    root = tk.Tk()
    app = RegistroWindow(root)
    root.mainloop()
