/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package problema02;

import java.util.Locale;
import java.util.Scanner;

/**
 *
 * @author DELL
 */
public class Problema02 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner entrada = new Scanner(System.in);
        entrada.useLocale(Locale.US);
        double porcentaje1 = 20;
        double porcentaje2 = 25;
        double porcentaje3 = 40;
        double porcentaje4 = 50;
        double descuento1;
        double descuento2;
        double descuento3;
        double descuento4;
        double descuento;
        int cantidad_trajes;
        double precio_trajes;
        double valor_total;
        double subtotal;

        System.out.println("ingrese la cantidad de trajes");
        cantidad_trajes = entrada.nextInt();
        System.out.println("ingrese el precio de los trajes");
        precio_trajes = entrada.nextDouble();

        subtotal = precio_trajes * cantidad_trajes;

        if (cantidad_trajes == 1) {
            descuento1 = (porcentaje1 * subtotal) / 100;
            valor_total = subtotal - descuento1;
            descuento = porcentaje1;
        } else {
            if (cantidad_trajes == 2) {
                descuento2 = (porcentaje2 * subtotal) / 100;
                valor_total = subtotal - descuento2;
                descuento = porcentaje2;

            } else {
                if (cantidad_trajes == 3) {
                    descuento3 = (subtotal * porcentaje3) / 100;
                    valor_total = subtotal - descuento3;
                    descuento = porcentaje3;

                } else {
                    descuento4 = subtotal * porcentaje4 / 100;
                    valor_total = subtotal - descuento4;
                    descuento = porcentaje4;

                }

            }
        }
        System.out.printf("El subtotal a pagar es %s\nEl descuento es %s\n"
                + "El total a pagar es %s\n", subtotal, descuento + "%",
                valor_total);

    }

}
