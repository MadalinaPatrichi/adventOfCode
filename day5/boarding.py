def getPos(ticket):
  lowRow = 0
  highRow = 127
  lowSeat = 0
  highSeat = 7
  for ch in ticket:
    if ch == 'B':
      lowRow = (lowRow+highRow)/2 + ((lowRow + highRow) % 2)
    elif ch == 'F':
      highRow = (highRow+lowRow)/2
    elif ch == 'R':
      lowSeat = (lowSeat + highSeat)/2 + (lowSeat + highSeat) % 2
    elif ch == 'L':
      highSeat = (lowSeat + highSeat)/2
  return (lowRow + highRow)/2, (lowSeat + highSeat)/2


with open('input', 'r') as file:
  boarding = list(file)
  highest = 0
  seats=[]
  for ticket in boarding:
    row, seat = getPos(ticket)
    seatId = row*8+seat
    seats.append(seatId)
    if seatId > highest:
      highest = seatId
  seats = sorted(seats)
  idx = 0
  while idx < len(seats):
    idx+=1
    if seats[idx-1] == (seats[idx] - 1) and seats[idx+1] == (seats[idx] + 1):
      continue
    else:
      print("Missing seat", seats[idx-1], seats[idx], seats[idx+1])
      break
