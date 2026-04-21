from services.excel_services import projetos_pendentes
from services.clickup_service import criar_tarefa_clickup
from utils.logger import log

log("Lendo Excel...")

dados = projetos_pendentes()

for _, row in dados.iterrows():
    criar_tarefa_clickup(
        nome=row["Projeto"],
        descricao=f"Responsável: {row['Responsável']}",
        prioridade=row["Prioridade"]
    )

    log(f"Tarefa criada para projeto: {row['Projeto']}")

log("Processo Concluído!")



