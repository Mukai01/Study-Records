import java.sql.*;

public class DBConnect2 {
    public static void main(String[] args) throws Exception {
    Connection con;
    Statement st;
    ResultSet rs;

    String url = "jdbc:postgresql://localhost:5432/shop";
    String user = "postgres";
    String password = "xxxx";

    Class.forName("org.postgresql.Driver");

    con = DriverManager.getConnection(url, user, password);
    st = con.createStatement();

    rs = st.executeQuery("SELECT shohin_id, shohin_mei FROM Shohin");

    while(rs.next()) {
        System.out.print(rs.getString("shohin_id") + ", ");
        System.out.println(rs.getString("shohin_mei"));
    }

    rs.close();
    st.close();
    con.close();
    }
}