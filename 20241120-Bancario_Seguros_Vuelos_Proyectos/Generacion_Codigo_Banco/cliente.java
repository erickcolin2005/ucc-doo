

/**
 * @version 1.0
 * @created 22-nov.-2024 6:37:23 a. m.
 */
public class cliente implements usuario {

	private int id_usuario;
	private string nombre;
	private string apellido;
	private string correo;
	private string telefono;
	private string direccion;
	private int rol;
	private cuenta_ahorro m_cuenta_ahorro;
	private prestamo_personal m_prestamo_personal;

	public cliente(){

	}

	public void finalize() throws Throwable {

	}

	public int registrarusuario(){
		return 0;
	}

	public int actualizardatos(){
		return 0;
	}

	public int gestionarcuenta(){
		return 0;
	}

}