package Exercicios.Interfaces;
public class Fatura {
    private double pricePerHour;
    private double pricePerDay;
    private BrasilTaxa taxaBrasil;

    public Fatura(double pricePerHour, double pricePerDay, BrasilTaxa taxaBrasil) {
        this.pricePerHour = pricePerHour;
        this.pricePerDay = pricePerDay;
        this.taxaBrasil = taxaBrasil;
    }

    public Fatura(double pricePerHour, double pricePerDay) {
        this.pricePerHour = pricePerHour;
        this.pricePerDay = pricePerDay;
    }
    public Fatura(){
    }

    public double getPricePerHour() {
        return pricePerHour;
    }

    public void setPricePerHour(double pricePerHour) {
        this.pricePerHour = pricePerHour;
    }

    public double getPricePerDay() {
        return pricePerDay;
    }

    public void setPricePerDay(double pricePerDay) {
        this.pricePerDay = pricePerDay;
    }

    public BrasilTaxa getTaxaBrasil() {
        return taxaBrasil;
    }

    public void setTaxaBrasil(BrasilTaxa taxaBrasil) {
        this.taxaBrasil = taxaBrasil;
    }

    //eu sei que isso tá feio, mas é 00:45 e eu tô caindo de sono
    public double processarFatura(double pricePerDay, double pricePerHour, BrasilTaxa taxaBrasil){
        return (pricePerDay + pricePerHour) * taxaBrasil.getTaxa() + pricePerDay + pricePerHour;
    }
    
}