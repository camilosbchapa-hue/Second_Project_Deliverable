public class Main {
    public static void main(String[] args) {
        // Un tablero de Sudoku válido de prueba (9x9)
        int[][] tablero = {
            {5, 3, 4, 6, 7, 8, 9, 1, 2},
            {6, 7, 2, 1, 9, 5, 3, 4, 8},
            {1, 9, 8, 3, 4, 2, 5, 6, 7},
            {8, 5, 9, 7, 6, 1, 4, 2, 3},
            {4, 2, 6, 8, 5, 3, 7, 9, 1},
            {7, 1, 3, 9, 2, 4, 8, 5, 6},
            {9, 6, 1, 5, 3, 7, 2, 8, 4},
            {2, 8, 7, 4, 1, 9, 6, 3, 5},
            {3, 4, 5, 2, 8, 6, 1, 7, 9}
        };

        boolean esValido = validarTablero(tablero);
        
        if (esValido) {
            System.out.println("¡El tablero es un Sudoku válido!");
        } else {
            System.out.println("El tablero tiene errores (números repetidos).");
        }
    }

    public static boolean validarTablero(int[][] tablero) {
        // 1. Validar todas las filas
        for (int fila = 0; fila < 9; fila++) {
            // Arreglo para marcar los números que ya vimos (del 1 al 9)
            // Usamos tamaño 10 para poder usar los índices del 1 al 9 directamente
            boolean[] numerosVistos = new boolean[10]; 
            
            for (int col = 0; col < 9; col++) {
                int numeroActual = tablero[fila][col];
                
                // Si el número ya fue visto en esta fila, es inválido
                if (numerosVistos[numeroActual] == true) {
                    return false; 
                }
                // Si no, lo marcamos como visto
                numerosVistos[numeroActual] = true;
            }
        }

        // 2. Validar todas las columnas
        for (int col = 0; col < 9; col++) {
            boolean[] numerosVistos = new boolean[10]; 
            
            for (int fila = 0; fila < 9; fila++) {
                int numeroActual = tablero[fila][col]; // Nota cómo se invierte fila y col aquí
                
                if (numerosVistos[numeroActual] == true) {
                    return false; 
                }
                numerosVistos[numeroActual] = true;
            }
        }

        // Si termina de revisar todo y no encontró repetidos, es válido
        return true; 
    }
}





