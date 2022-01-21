# leaky bucket

class LeakyBucket:
  def __init__(self, size, input_stream, output_rate):
    self.size = size
    self.queue = input_stream
    self.flow = output_rate

  def congestion_control(self):
    storage = 0
    for i in range(len(self.queue)):
      sizeleft = self.size - storage
      if self.queue[i] <= sizeleft:
        storage += self.queue[i]
        print('input packet sent: {}, buffer size: {}'.format(self.queue[i], storage))
      else:
        storage = self.size
        print('input packet sent: {}, buffer size: {}, packet lost: {}'.format(self.queue[i], storage, self.queue[i] - sizeleft))
      storage = storage - self.flow

def main():
  queue = [4, 4, 4, 4]

  leakybucket = LeakyBucket(10, queue, 1)
  leakybucket.congestion_control()

main()
