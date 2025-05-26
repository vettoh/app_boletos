from datetime import datetime

def formatar_data_vencimento(data_venc):
    """converte data em string para datetime.date"""
    try: 
        if "/" in data_venc:
            return datetime.strptime(data_venc, "%d/%m/%Y").date ()
        elif "-" in data_venc:
            return datetime.strptime(data_venc, "%Y-%m-%d").date()
    except ValueError:
        return None    