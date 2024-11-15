package System;


/**
 * @version 1.0
 * @created 15-nov.-2024 9:04:12 a. m.
 */
public class Lector implements IAutenticable {

	private int id_lector;
	private String tipo_lector;
	public Puerta m_Puerta;

	public Lector(){

	}

	public void finalize() throws Throwable {

	}

	/**
	 * 
	 * @param id_credencial
	 */
	public boolean leerCredencial(int id_credencial){
		return false;
	}

	/**
	 * 
	 * @param id_credencial
	 */
	public boolean acceder(int id_credencial){
		return false;
	}

	public boolean activar(){
		return false;
	}

	public boolean revocar(){
		return false;
	}

	/**
	 * 
	 * @param id_credencial
	 */
	public boolean verificarAcceso(int id_credencial){
		return false;
	}

}