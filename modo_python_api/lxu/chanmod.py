'''Autogenerated dummy chanmod module anabling code completion in Python editors
 MODO Build #569521
'''


class InternalChanModOperator:
    def cmop_Evaluate(self):
        pass


class MetaPackage:
    def cman_Allocate(self, cmod):
        pass

    def cman_Define(self, cmod):
        pass

    def operator(self):
        '''The sub-class must implement this and return a new instance of their
        Operator.
        '''
        pass

    def pkg_Attach(self):
        pass

    def pkg_CollectItems(self, collection, mode):
        pass

    def pkg_PostLoad(self, scene):
        pass

    def pkg_SetupChannels(self, add_obj):
        pass

    def pkg_TestInterface(self, guid):
        pass


class Operator:
    def eval(self, chans):
        '''The eval() method reads from input channels and writes to output channels.
        This computes the result of the modifier.
        '''
        pass

    def initialize(self, desc):
        '''The intialize() method takes an AttributeDesc object and should define
        the channels and the channel modifier inputs and outputs.
        '''
        pass

    def post_alloc(self, chans):
        '''The post_alloc() method is optional, and is called right after the values
        are bound.
        '''
        pass


def bless_server(classref, name):
    '''This is a replacement for blessing channel modifier classes that just provides
       standard tags.
    '''
    pass
