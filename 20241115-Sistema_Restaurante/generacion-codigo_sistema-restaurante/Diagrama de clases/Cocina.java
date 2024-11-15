

/**
 * @version 1.0
 * @created 15-nov.-2024 11:42:56 a. m.
 */
public class Cocina implements IOrdenable {

	private int id_cocina;
	public Orden m_Orden;
	public Inventario m_Inventario;

	public Cocina(){

	}

	public void finalize() throws Throwable {

	}

	/**
	 * 
	 * @param orden
	 */
	public Void recibirOrden(Orden orden){

	}

	/**
	 * 
	 * @param orden
	 */
	public Void tomarOrden(Orden orden){

	}

	/**
	 * 
	 * @param plato
	 */
	public Void prepararPlato(Plato plato){

	}

	/**
	 * 
	 * @param nuevoEstado
	 */
	public Void actualizarEstado(String nuevoEstado){

	}

}