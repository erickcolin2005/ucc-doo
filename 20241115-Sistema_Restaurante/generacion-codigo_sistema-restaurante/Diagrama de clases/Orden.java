

/**
 * @version 1.0
 * @created 15-nov.-2024 11:42:56 a. m.
 */
public class Orden {

	private int id_orden;
	private Date fecha;
	private String estado;
	private double total;
	public Plato m_Plato;

	public Orden(){

	}

	public void finalize() throws Throwable {

	}

	public double calcularTotal(){
		return 0;
	}

	/**
	 * 
	 * @param nuevoEstado
	 */
	public Void actualizarEstado(String nuevoEstado){

	}

}