# 📬 App Boletos - Gerenciador e Alerta de Vencimentos

Este é um aplicativo desktop feito com **Python + Tkinter** para cadastrar boletos e **enviar alertas por e-mail** automaticamente quando estiverem próximos do vencimento.

> 🔔 O sistema verifica os boletos cadastrados e envia um e-mail automático **1 dia antes** do vencimento!

---

## 🚀 Funcionalidades

- Cadastro de boletos com:
  - Nome do cliente
  - Data do pedido
  - Valor total
  - Quantidade de parcelas
  - Data de vencimento
- Armazenamento local com SQLite
- Envio automático de e-mails com alerta de vencimento (via `smtplib`)
- Interface gráfica com Tkinter
- Agendador de tarefas com `schedule`

---

## 🖼️ Interface

*(Adicione aqui uma imagem do app rodando quando possível)*

---

## 🛠️ Tecnologias utilizadas

- Python 3.12
- Tkinter (interface gráfica)
- SQLite (banco de dados local)
- `smtplib` (envio de e-mail)
- `schedule` (agendamento de tarefas)
- `threading` (execução em segundo plano)

---

## ⚙️ Como rodar o projeto

1. **Clone o repositório:**
```bash
git clone https://github.com/vettoh/app_boletos.git
cd app_boletos
