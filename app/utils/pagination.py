from typing import Dict, Any

def create_pagination_response(
    data: list,
    offset: int,
    limit: int,
    total_count: int = None
) -> Dict[str, Any]:
    """Create standardized pagination response"""
    previous = max(0, offset - limit) if offset > 0 else None
    next_offset = offset + limit if len(data) == limit else None
    
    page_info = {
        "limit": limit,
        "offset": offset,
        "next": next_offset,
        "previous": previous
    }
    
    if total_count is not None:
        page_info["total"] = total_count
    
    return {
        "data": data,
        "page": page_info
    }

def validate_pagination_params(offset: int, limit: int) -> tuple[int, int]:
    """Validate and normalize pagination parameters"""
    offset = max(0, offset)
    limit = max(1, min(100, limit))  
    return offset, limit
