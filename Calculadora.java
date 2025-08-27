import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.*;

public class Calculadora extends JFrame implements ActionListener {

    private JTextField pantalla;
    private double num1 = 0, num2 = 0;
    private String operador = "";
    private boolean nuevoNumero = true;

    public Calculadora() {
        setTitle("Calculadora");
        setSize(300, 400);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setLayout(new BorderLayout());

        pantalla = new JTextField("0");
        pantalla.setEditable(false);
        pantalla.setFont(new Font("Arial", Font.BOLD, 28));
        pantalla.setHorizontalAlignment(JTextField.RIGHT);
        add(pantalla, BorderLayout.NORTH);

        JPanel panelBotones = new JPanel();
        panelBotones.setLayout(new GridLayout(4, 4, 5, 5));

        String[] botones = {
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", "C", "=", "+"
        };

        for (String texto : botones) {
            JButton boton = new JButton(texto);
            boton.setFont(new Font("Arial", Font.BOLD, 20));
            boton.addActionListener(this);
            panelBotones.add(boton);
        }

        add(panelBotones, BorderLayout.CENTER);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        String comando = e.getActionCommand();

        if (comando.matches("[0-9]")) {
            if (nuevoNumero) {
                pantalla.setText(comando);
                nuevoNumero = false;
            } else {
                pantalla.setText(pantalla.getText() + comando);
            }
        } else if (comando.matches("[+\\-*/]")) {
            num1 = Double.parseDouble(pantalla.getText());
            operador = comando;
            nuevoNumero = true;
        } else if (comando.equals("=")) {
            num2 = Double.parseDouble(pantalla.getText());
            double resultado = 0;

            switch (operador) {
                case "+": resultado = num1 + num2; break;
                case "-": resultado = num1 - num2; break;
                case "*": resultado = num1 * num2; break;
                case "/":
                    if (num2 != 0) {
                        resultado = num1 / num2;
                    } else {
                        pantalla.setText("Error");
                        nuevoNumero = true;
                        return;
                    }
                    break;
            }

            pantalla.setText(String.valueOf(resultado));
            nuevoNumero = true;
            operador = "";
        } else if (comando.equals("C")) {
            pantalla.setText("0");
            num1 = 0;
            num2 = 0;
            operador = "";
            nuevoNumero = true;
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            new Calculadora().setVisible(true);
        });
    }
}
