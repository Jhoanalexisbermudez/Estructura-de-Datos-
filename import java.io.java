import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class MiniColaboracionGit {

    public static void main(String[] args) {
        // Crear carpeta "session-1"
        String folderName = "session-1";
        File folder = new File(folderName);
        if (!folder.exists()) {
            folder.mkdir();
            System.out.println("Carpeta 'session-1' creada.");
        }

        // Datos de los dos integrantes
        String[][] miembros = {
            {"Jhon Alex Ante", "18", "Desarrollo de Software", "4", "Me gusta coleccionar tapas de botellas", "Azul", "Sí, un gato", "Desarrollo web y videojuegos"},
            {"Jhoan Alexis Bermudez", "20", "Desarrollo de Software", "4", "Me gusta ver videos de teorías conspirativas", "Verde", "No", "Apps móviles y backend"}
        };

        // Crear archivos con información personal
        for (String[] persona : miembros) {
            String nombreArchivo = persona[0].toLowerCase().replace(" ", "_") + ".txt";
            File archivo = new File(folderName + File.separator + nombreArchivo);
            
            try (BufferedWriter writer = new BufferedWriter(new FileWriter(archivo))) {
                writer.write("Nombre: " + persona[0] + "\n");
                writer.write("Edad: " + persona[1] + "\n");
                writer.write("Programa académico: " + persona[2] + "\n");
                writer.write("Semestre actual: " + persona[3] + "\n");
                writer.write("Algo extraño que te gusta hacer: " + persona[4] + "\n");
                writer.write("Color favorito: " + persona[5] + "\n");
                writer.write("¿Tienes mascotas? (¿cuáles?): " + persona[6] + "\n");
                writer.write("Intereses en el desarrollo de software: " + persona[7] + "\n");
                System.out.println("Archivo creado: " + nombreArchivo);
            } catch (IOException e) {
                System.err.println("Error al escribir el archivo " + nombreArchivo);
                e.printStackTrace();
            }
        }

        System.out.println("Todos los archivos fueron creados exitosamente.");
    }
}
