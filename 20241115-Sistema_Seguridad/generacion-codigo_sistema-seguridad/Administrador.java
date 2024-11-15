package System;


/**
 * @version 1.0
 * @created 15-nov.-2024 9:04:25 a. m.
 */
public class Administrador implements IGestionable, IAlertable {

	private int id_administrador;
	private String nombre;

	public Administrador(){

	}

	public void finalize() throws Throwable {

	}

	/**
	 * 
	 * @param tipo
	 */
	public Credencial crearCredencial(String tipo){
		return null;
	}

	/**
	 * 
	 * @param id_credencial
	 */
	public boolean eliminarCredencial(int id_credencial){
		return false;
	}

	/**
	 * 
	 * @param mensaje
	 */
	public Void emitirAlerta(String mensaje){

	}

}