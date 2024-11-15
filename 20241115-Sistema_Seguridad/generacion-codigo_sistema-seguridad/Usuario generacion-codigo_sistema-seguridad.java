package System;


/**
 * @version 1.0
 * @created 15-nov.-2024 9:00:32 a. m.
 */
public class Usuario {

	private int id_usuario;
	private String nombre;
	private String tipo_credencial;
	public Credencial m_Credencial;

	public Usuario(){

	}

	public void finalize() throws Throwable {

	}

	/**
	 * 
	 * @param id_credencial
	 */
	public boolean acceder(int id_credencial){
		return false;
	}

	public boolean registrarSalida(){
		return false;
	}

}