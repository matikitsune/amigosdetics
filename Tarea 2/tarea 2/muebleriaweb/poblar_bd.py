from curso.models import proyecto

proyecto = proyecto(descripcion="Este es un proyecto para el curso IN3501",
	cliente="CEI", fecha_limite="2018-06-20")
proyecto.save()