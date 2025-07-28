package sdoforbiz.ru.prser

import android.os.Bundle
import android.widget.*
import androidx.appcompat.app.AppCompatActivity
import androidx.lifecycle.lifecycleScope
import org.json.JSONArray
import java.net.HttpURLConnection
import java.net.URL
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        val searchBtn = findViewById<Button>(R.id.searchBtn)
        val queryEdit = findViewById<EditText>(R.id.queryEdit)
        val resultView = findViewById<TextView>(R.id.resultView)

        searchBtn.setOnClickListener {
            val query = queryEdit.text.toString()
            if (query.isBlank()) {
                Toast.makeText(this, "Введите название продукта", Toast.LENGTH_SHORT).show()
                return@setOnClickListener
            }
            resultView.text = "Поиск..."
            lifecycleScope.launch {
                val results = withContext(Dispatchers.IO) {
                    try {
                        val url = URL("http://ВАШ_IP_ИЛИ_ДОМЕН:5000/api/search")
                        val conn = url.openConnection() as HttpURLConnection
                        conn.requestMethod = "POST"
                        conn.setRequestProperty("Content-Type", "application/json")
                        conn.doOutput = true
                        conn.outputStream.write("""{"query":"$query"}""".toByteArray())
                        val response = conn.inputStream.bufferedReader().readText()
                        JSONArray(response)
                    } catch (e: Exception) {
                        null
                    }
                }
                if (results != null) {
                    val sb = StringBuilder()
                    for (i in 0 until results.length()) {
                        val obj = results.getJSONObject(i)
                        sb.append("${obj.getString("site")}: ${obj.getString("price")}\n${obj.getString("url")}\n\n")
                    }
                    resultView.text = sb.toString()
                } else {
                    resultView.text = "Ошибка поиска или нет данных"
                }
            }
        }
    }
}