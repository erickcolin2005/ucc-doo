package System;


/**
 * @version 1.0
 * @created 15-nov.-2024 9:04:54 a. m.
 */
public interface IAutenticable {

	/**
	 * 
	 * @param id_credencial
	 */
	public boolean verificarAcceso(int id_credencial);

}