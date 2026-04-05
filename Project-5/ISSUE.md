# 🐳 Docker Networking Confusion with Host Mode

## 📌 Issue Summary

While running a container using host network mode, the application was accessible from the EC2 instance even though the port was changed in the application code but not updated in the Dockerfile.

---

## 🔍 What Happened

* Updated application port in `app.py`:

  ```python
  port = 6100
  ```
* Dockerfile still had old port (e.g., `EXPOSE 6000`)
* Ran container using:

  ```bash
  docker run -d --name container2 --network host app2
  ```
* Application was still accessible via:

  ```
  http://<EC2-IP>:6100
  ```

---

## 🤔 Why It Worked

* `--network host` makes the container use the **host’s network directly**
* No port mapping (`-p`) is required
* The app binds directly to the EC2 instance port (`6100`)
* Dockerfile `EXPOSE` instruction is only documentation and has no effect here

---

## ⚠️ Key Observations

* Container and host share the same network namespace
* Application port becomes directly accessible on EC2
* No isolation between host and container networking
* Port conflicts may occur if multiple containers use the same port

---

## ✅ Correct Understanding

| Component        | Behavior                    |
| ---------------- | --------------------------- |
| `app.py`         | Defines actual running port |
| `EXPOSE`         | Informational only          |
| `--network host` | Bypasses Docker networking  |
| `-p` mapping     | Not required in host mode   |

---

## 💡 Best Practice

* Avoid using `--network host` in production unless necessary
* Use bridge networking with explicit port mapping:

  ```bash
  docker run -p 6100:6100 app2
  ```
* Keep ports consistent across application and Docker configuration

---

## 🎯 Conclusion

The application was accessible because host networking allowed the container to directly bind to the EC2 port, bypassing Docker’s standard networking and port mapping mechanisms.

---
