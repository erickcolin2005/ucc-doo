

/**
 * @author SERVIDOR
 * @version 1.0
 * @created 22-nov.-2024 6:37:27 a. m.
 */
public class prestamo_personal implements prestamo {

	private int id_prestamo;
	private int id_usuario;
	private double monto;
	private int plazo;
	private string estado;
	private localdetime fecha_solicitud;

	public prestamo_personal(){

	}

	public void finalize() throws Throwable {

	}

	public int solicitarprestamo(){
		return 0;
	}

	public int aprobarprestamo(){
		return 0;
	}

}