package Exercicios.Interfaces;
public class BrasilTaxa {
    private double taxa;

    public BrasilTaxa() {
    }

    public double getTaxa() {
        return taxa;
    }

    public void setTaxa(double taxa) {
        this.taxa = (taxa / 100);
    }
    
}
