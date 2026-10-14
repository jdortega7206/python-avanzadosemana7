"""Punto de entrada del proyecto.

Permite ejecutar la aplicación completa o importar los módulos individualmente.
"""

import sys


def mostrar_menu() -> None:
    """Muestra un menú simple para elegir qué interfaz ejecutar."""
    print("\n" + "=" * 50)
    print("   MÓDULO DE AUTENTICACIÓN CON TKINTER")
    print("=" * 50)
    print("\nSeleccione una opción:")
    print("  1. Ejecutar Interfaz de Inicio de Sesión (login)")
    print("  2. Ejecutar Interfaz de Registro de Clientes")
    print("  3. Salir\n")

    opcion = input("Ingrese el número de la opción: ")

    if opcion == "1":
        from login import LoginWindow
        root = tk.Tk()
        app = LoginWindow(root)
        root.mainloop()
    elif opcion == "2":
        from registro import RegistroWindow
        root = tk.Tk()
        app = RegistroWindow(root)
        root.mainloop()
    else:
        print("Saliendo del programa...")


if __name__ == "__main__":
    import tkinter as tk

    mostrar_menu()
