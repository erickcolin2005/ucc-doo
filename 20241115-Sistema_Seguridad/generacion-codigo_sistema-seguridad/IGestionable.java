package System;


/**
 * @version 1.0
 * @created 15-nov.-2024 9:04:35 a. m.
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