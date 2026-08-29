package Exercicios.Interfaces;
public class BrasilTaxa implements TaxaGeral {
    private double taxa;

    public BrasilTaxa() {
    }

    public double getTaxa() {
        return taxa;
    }

    @Override
    public double calcularTaxa(double taxa) {
        return (taxa / 100) + 1; 
    }
    
}
