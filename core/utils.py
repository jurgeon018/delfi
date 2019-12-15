


def get_sk(request):
  sk = request.session.session_key
  if not sk: request.session.cycle_key()
  return sk
