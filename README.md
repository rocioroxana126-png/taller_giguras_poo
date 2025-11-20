# Taller Figuras Geométricas (POO – Python)
Este proyecto implementa una jerarquía de clases usando Programación Orientada a Objetos, aplicando:

- Encapsulamiento con `@property` y setters  
- Herencia  
- Polimorfismo  
- Sobrescritura de métodos  
- Validaciones internas  
- Estándar PEP8  


 Descripción de las clases

 FiguraGeometrica
Clase base abstracta con:
- Atributos privados `_ancho` y `_alto`
- Getters y setters con validación
- Método `area()`
- Método abstracto `perimetro()`
- `__str__` personalizado

 Cuadrado
Hereda de `FiguraGeometrica`  
Sobrescribe:
- `area()`
- `perimetro()`
- `__str__()`

 Rectangulo
Hereda de `FiguraGeometrica`  
Sobrescribe:
- `area()`
- `perimetro()`
- `__str__()`

 Ejecución

El archivo `main.py`:

- Crea 2 cuadrados y 2 rectángulos
- Demuestra encapsulamiento (errores)
- Modifica valores correctamente
- Imprime área, perímetro y el objeto
- Calcula suma de áreas y perímetros usando polimorfismo

 Evidencia de Ejecución
<img width="1360" height="768" alt="Captura de pantalla 2025-11-20 003327" src="https://github.com/user-attachments/assets/b187f4d1-a340-46bf-b330-398bd12084d7" />
<img width="1360" height="768" alt="Captura de pantalla 2025-11-20 003302" src="https://github.com/user-attachments/assets/24e6e95a-50f5-455c-bc00-22d48bfa68ce" />
<img width="1360" height="768" alt="Captura de pantalla 2025-11-20 003249" src="https://github.com/user-attachments/assets/c2014fb8-0538-4959-b066-a5691fd05dfb" />


