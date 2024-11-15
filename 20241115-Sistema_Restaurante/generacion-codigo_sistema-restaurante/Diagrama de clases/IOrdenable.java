

/**
 * @version 1.0
 * @created 15-nov.-2024 11:42:56 a. m.
 */
public interface IOrdenable {

	/**
	 * 
	 * @param orden
	 */
	public Void tomarOrden(Orden orden);

	/**
	 * 
	 * @param orden
	 */
	public Void recibirOrden(Orden orden);

	/**
	 * 
	 * @param nuevoEstado
	 */
	public Void actualizarEstado(String nuevoEstado);

}