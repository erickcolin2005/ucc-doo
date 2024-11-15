

/**
 * @version 1.0
 * @created 15-nov.-2024 11:42:56 a. m.
 */
public class Mesero implements IOrdenable, IReporteable {

	private int id_mesero;
	private int nombre;
	public Ciente m_Ciente;
	public Cocina m_Cocina;
	public Pago m_Pago;
	public Administrador m_Administrador;

	public Mesero(){

	}

	public void finalize() throws Throwable {

	}

	public String generarInformeDiario(){
		return "";
	}

	/**
	 * 
	 * @param orden
	 */
	public Void tomarOrden(Orden orden){

	}

	/**
	 * 
	 * @param pago
	 */
	public boolean procesarPago(Pago pago){
		return false;
	}

	/**
	 * 
	 * @param orden
	 */
	public Void recibirOrden(Orden orden){

	}

	/**
	 * 
	 * @param nuevoEstado
	 */
	public Void actualizarEstado(String nuevoEstado){

	}

	/**
	 * 
	 * @param plato
	 */
	public Orden realizarPedido(Plato plato){
		return null;
	}

	public totalCalculado(){

	}

	public preparacionCompletada(){

	}

}