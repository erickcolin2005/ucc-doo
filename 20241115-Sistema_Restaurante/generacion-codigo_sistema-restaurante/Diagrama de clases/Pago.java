

/**
 * @version 1.0
 * @created 15-nov.-2024 11:42:56 a. m.
 */
public class Pago implements IPagable {

	private int id_pago;
	private double monto;
	private Date fecha;
	private String metodo;
	public Orden m_Orden;

	public Pago(){

	}

	public void finalize() throws Throwable {

	}

	public boolean procesarPago(){
		return false;
	}

}