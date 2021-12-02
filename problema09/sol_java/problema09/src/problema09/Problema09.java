/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package problema09;

import java.util.Locale;
import java.util.Scanner;

/**
 *
 * @author DELL
 */
public class Problema09 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
   Scanner entrada = new Scanner(System.in);
        entrada.useLocale(Locale.US);

        int limite = 44;
        int val1 = 12;
        int val2 = 11;

       
        do {

            System.out.printf("+%s-%s", val1, val2);
            val1 = val1 + 12;
            val2 = val2 + 11;

        } while (val2 <= limite);

    
    
    
    }
    
}
