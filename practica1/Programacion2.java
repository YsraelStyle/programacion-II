/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package programacion2;

class Punto {
    private double x;
    private double y;

    public Punto(double x, double y) {
        this.x = x;
        this.y = y;
    }

    
    public double[] coordCartesianas() {
        return new double[]{x, y};
    }

    
    public double[] coordPolares() {
        double radio = Math.sqrt(x * x + y * y);
        double angulo = Math.atan2(y, x);
        return new double[]{radio, angulo};
    }

    
    public String toString() {
        return "(" + x + ", " + y + ")";
    }
}

public class Programacion2 {
    public static void main(String[] args) {
        Punto p1 = new Punto(2, 3);

        double[] coordCart = p1.coordCartesianas();
        System.out.println("Coordenadas Cartesianas: " + coordCart[0] + ", " + coordCart[1]);

        double[] coordPol = p1.coordPolares();
        System.out.println("Coordenadas Polares: " + coordPol[0] + ", " + coordPol[1]);
    }
}

