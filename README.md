# Projetto Flask — testes com GitHub Actions

Aplicacao Flask simples que retorna uma lista de tarefas no endpoint `GET /`.
O codigo da aplicacao foi baseado no arquivo fornecido.

## Testes automatizados

O workflow em `.github/workflows/testes.yml` executa:

- Verificacao da sintaxe Python.
- Teste de resposta HTTP 200.
- Teste de resposta JSON.
- Teste do conteudo das tarefas retornadas.
- Teste da quantidade de tarefas.

## Quando os testes executam

- Em todo `push`.
- Em Pull Requests.
- Manualmente em **Actions → Testes automaticos do Flask → Run workflow**.
- A cada 6 horas (cron em UTC).

## Executar localmente

```bash
python -m pip install -r requirements.txt
python -m pytest -v
python app.py
```

A aplicacao fica disponivel localmente em `http://localhost:5000/`.

> O GitHub Actions executa os testes e encerra o job. Ele nao hospeda o servidor Flask continuamente.
