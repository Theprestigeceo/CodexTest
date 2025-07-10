from fastapi import APIRouter

router = APIRouter()

@router.get("/playbooks")
async def get_playbooks():
    """Placeholder for sales playbooks."""
    return {"status": "Sales playbooks coming soon"}
