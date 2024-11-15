package System;


/**
 * @version 1.0
 * @created 15-nov.-2024 9:29:31 a. m.
 */
public interface IGestionable {

	/**
	 * 
	 * @param tipo
	 */
	public Credencial crearCredencial(String tipo);

	/**
	 * 
	 * @param id_credencial
	 */
	public boolean eliminarCredencial(int id_credencial);

}